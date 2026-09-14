#!/usr/bin/env python3
"""Release-oriented static checks for Age of Empires – RT56 Edition.

Run from any directory:
    python tools/validate_aoeiw.py
    python tools/validate_aoeiw.py --vanilla "C:/.../Hearts of Iron IV"

The validator deliberately reports only conditions it can prove from source.
It does not pretend to replace an in-game fresh-start test or error.log review.
"""

from __future__ import annotations

import argparse
import bisect
import collections
import json
import re
import sys
from pathlib import Path


TOKEN = re.compile(r'#[^\n]*|"(?:\\.|[^"\\])*"|[{}]|[=<>!]+|[^\s{}=<>!"#]+')
SCRIPT_FOLDERS = ("common", "events", "history", "interface", "map", "sound")
SCRIPT_SUFFIXES = {".txt", ".gui", ".gfx", ".asset", ".mod"}


def is_aoe(value: str) -> bool:
    return bool(re.search(r"aoeiw|age_of_empires", value, re.I))


def parse_script(path: Path):
    source = path.read_text(encoding="utf-8-sig", errors="replace")
    newlines = [match.start() for match in re.finditer("\n", source)]
    tokens = [
        (match.group(), bisect.bisect_left(newlines, match.start()) + 1)
        for match in TOKEN.finditer(source)
        if not match.group().startswith("#")
    ]
    root: list = []
    stack = [root]
    issues = []
    index = 0
    while index < len(tokens):
        value, line = tokens[index]
        if value == "}":
            if len(stack) == 1:
                issues.append((line, "extra closing brace"))
            else:
                stack.pop()
            index += 1
            continue
        if index + 2 < len(tokens) and tokens[index + 1][0] in {
            "=", ">", "<", ">=", "<=", "!=", "?="
        }:
            target = tokens[index + 2][0]
            node = [value.strip('"'), target.strip('"'), line, []]
            stack[-1].append(node)
            if target == "{":
                stack.append(node[3])
            index += 3
            continue
        if value == "{":
            node = ["<bare>", "{", line, []]
            stack[-1].append(node)
            stack.append(node[3])
        else:
            stack[-1].append(["<value>", value.strip('"'), line, []])
        index += 1
    if len(stack) > 1:
        issues.append((0, f"{len(stack) - 1} unclosed block(s)"))
    return root, issues


def walk(nodes, parent=""):
    for node in nodes:
        yield node, parent
        yield from walk(node[3], node[0])


def prop(node, key):
    return next((child[1] for child in node[3] if child[0] == key), None)


def files_under(root: Path):
    for folder in SCRIPT_FOLDERS:
        base = root / folder
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.is_file() and path.suffix.lower() in SCRIPT_SUFFIXES:
                yield path


def collect_localisation(root: Path):
    keys = collections.defaultdict(list)
    malformed = []
    for path in (root / "localisation").rglob("*.yml"):
        data = path.read_bytes()
        text = data.decode("utf-8-sig", errors="replace")
        relative = path.relative_to(root).as_posix()
        if is_aoe(path.name) and not data.startswith(b"\xef\xbb\xbf"):
            malformed.append((relative, 1, "AOE localisation lacks UTF-8 BOM"))
        if is_aoe(path.name) and not re.match(r"\s*l_\w+:", text):
            malformed.append((relative, 1, "AOE localisation lacks language header"))
        if "l_english" not in path.name:
            continue
        for line_number, line in enumerate(text.splitlines(), 1):
            match = re.match(r'\s*([^\s:#]+):\d*\s+"', line)
            if match:
                keys[match.group(1)].append((relative, line_number))
    return keys, malformed


def collect_sprite_names(*roots: Path):
    names = set()
    pattern = re.compile(r'\bname\s*=\s*"?(GFX_[A-Za-z0-9_.:-]+)')
    for root in roots:
        for path in root.rglob("*.gfx"):
            text = path.read_text(encoding="utf-8-sig", errors="ignore")
            names.update(pattern.findall(text))
    return names


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--vanilla", type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    if not (root / "descriptor.mod").exists():
        parser.error(f"{root} is not an HOI4 mod root (descriptor.mod missing)")

    parsed = {}
    findings = collections.defaultdict(list)
    for path in files_under(root):
        relative = path.relative_to(root).as_posix()
        nodes, syntax = parse_script(path)
        parsed[relative] = nodes
        for line, message in syntax:
            findings["syntax"].append((relative, line, message))

    localisation, malformed = collect_localisation(root)
    findings["localisation_format"].extend(malformed)

    definitions = collections.defaultdict(lambda: collections.defaultdict(list))
    event_references = []
    focus_references = []
    focus_position_references = []
    oob_references = []
    decision_names = []
    localisation_requirements = []
    event_text = []
    state_provinces = collections.defaultdict(list)
    region_provinces = collections.defaultdict(list)

    for relative, nodes in parsed.items():
        for node, parent in walk(nodes):
            key, value, line, children = node
            site = (relative, line)
            if key in {"country_event", "news_event", "state_event"} and value == "{":
                event_id = prop(node, "id")
                if event_id:
                    if relative.startswith("events/") and parent == "":
                        definitions["event"][event_id].append(site)
                        if is_aoe(relative):
                            for child in children:
                                if child[0] in {"title", "desc"} and child[1] != "{":
                                    event_text.append((child[1], relative, child[2]))
                                if child[0] == "option":
                                    option_name = prop(child, "name")
                                    if option_name:
                                        event_text.append((option_name, relative, child[2]))
                    else:
                        event_references.append((event_id, relative, line))
            if key in {"country_event", "news_event", "state_event"} and value != "{":
                event_references.append((value, relative, line))
            if key in {"focus", "shared_focus", "joint_focus"} and value == "{":
                focus_id = prop(node, "id")
                if focus_id:
                    definitions["focus"][focus_id].append(site)
                    if is_aoe(focus_id):
                        for loc_key in (focus_id, f"{focus_id}_desc"):
                            if loc_key not in localisation:
                                findings["missing_localisation"].append(
                                    (relative, line, loc_key)
                                )
            if key in {"has_completed_focus", "focus"} and value != "{":
                focus_references.append((value, relative, line))
            if key == "relative_position_id" and value != "{":
                focus_position_references.append((value, relative, line))
            if key in {"oob", "load_oob", "load_naval_oob", "load_air_oob"} and value != "{":
                oob_references.append((value, relative, line))
            if relative.startswith("history/states/") and key == "id" and parent == "state":
                definitions["state"][value].append(site)
            if relative.startswith("history/states/") and key == "provinces":
                for child in children:
                    if child[0] == "<value>":
                        state_provinces[child[1]].append(relative)
            if relative.startswith("map/strategicregions/") and key == "id" and parent == "strategic_region":
                definitions["region"][value].append(site)
            if relative.startswith("map/strategicregions/") and key == "provinces":
                for child in children:
                    if child[0] == "<value>":
                        region_provinces[child[1]].append(relative)
            if relative.startswith("common/scripted_effects/") and parent == "":
                definitions["scripted_effect"][key].append(site)
            if relative.startswith("common/scripted_triggers/") and parent == "":
                definitions["scripted_trigger"][key].append(site)
            if (
                relative.startswith("common/dynamic_modifiers/")
                and parent == ""
                and value == "{"
                and is_aoe(key)
            ):
                definitions["dynamic_modifier"][key].append(site)
                localisation_requirements.extend(
                    [(key, relative, line), (f"{key}_desc", relative, line)]
                )
            if (
                relative.startswith("common/ideas/")
                and parent in {"country", "hidden_ideas"}
                and value == "{"
                and is_aoe(key)
                and any(child[0] in {"picture", "modifier", "allowed", "removal_cost", "research_production"} for child in children)
            ):
                definitions["idea"][key].append(site)
                localisation_requirements.extend(
                    [(key, relative, line), (f"{key}_desc", relative, line)]
                )
            if (
                relative.startswith("common/decisions/categories/")
                and parent == ""
                and value == "{"
                and is_aoe(key)
            ):
                definitions["decision_category"][key].append(site)
                localisation_requirements.append((key, relative, line))
            if (
                relative.startswith("common/decisions/")
                and "/categories/" not in relative
                and parent != ""
                and value == "{"
                and is_aoe(key)
            ):
                decision_names.append((key, relative, line))
                definitions["decision"][key].append(site)

    if args.vanilla:
        vanilla = args.vanilla.resolve()
        if not (vanilla / "common").exists():
            parser.error(f"Vanilla path does not contain common/: {vanilla}")
        for path in files_under(vanilla):
            relative = f"<vanilla>/{path.relative_to(vanilla).as_posix()}"
            nodes, _ = parse_script(path)
            for node, parent in walk(nodes):
                key, value, line, _ = node
                if key in {"country_event", "news_event", "state_event"} and value == "{" and parent == "":
                    event_id = prop(node, "id")
                    if event_id:
                        definitions["event"][event_id].append((relative, line))
                if key in {"focus", "shared_focus", "joint_focus"} and value == "{":
                    focus_id = prop(node, "id")
                    if focus_id:
                        definitions["focus"][focus_id].append((relative, line))

        # Asset checks need the base-game/DLC sprite registry to avoid reporting
        # valid vanilla references as missing from this standalone package.
        sprite_names = collect_sprite_names(root, vanilla)
        direct_sprite = re.compile(
            r'\b(?:icon|picture|large|small)\s*=\s*"?(GFX_[A-Za-z0-9_.:-]+)'
        )
        for path in files_under(root):
            relative = path.relative_to(root).as_posix()
            if not is_aoe(relative):
                continue
            source = path.read_text(encoding="utf-8-sig", errors="ignore")
            newlines = [match.start() for match in re.finditer("\n", source)]
            for match in direct_sprite.finditer(source):
                sprite = match.group(1)
                if sprite not in sprite_names:
                    line = bisect.bisect_left(newlines, match.start()) + 1
                    findings["missing_assets"].append((relative, line, sprite))
        for identifier, sites in definitions["idea"].items():
            relative, line = sites[0]
            idea_nodes = parsed.get(relative, [])
            for node, _ in walk(idea_nodes):
                if node[0] != identifier or node[2] != line:
                    continue
                picture = prop(node, "picture")
                if picture and not picture.startswith("GFX_"):
                    sprite = f"GFX_idea_{picture}"
                    if sprite not in sprite_names:
                        findings["missing_assets"].append((relative, line, sprite))
                break
        for relative, nodes in parsed.items():
            if not relative.startswith("common/decisions/") or not is_aoe(relative):
                continue
            for node, parent in walk(nodes):
                if parent == "" or node[1] != "{" or not is_aoe(node[0]):
                    continue
                icon = prop(node, "icon")
                if icon and not icon.startswith("GFX_"):
                    sprite = f"GFX_decision_{icon}"
                    if sprite not in sprite_names:
                        findings["missing_assets"].append((relative, node[2], sprite))

    for kind in (
        "event", "focus", "state", "region", "scripted_effect", "scripted_trigger",
        "dynamic_modifier", "idea", "decision_category", "decision",
    ):
        for identifier, sites in definitions[kind].items():
            local_sites = [site for site in sites if not site[0].startswith("<vanilla>/")]
            if len(local_sites) > 1:
                findings["duplicate_ids"].append((kind, identifier, local_sites))

    for identifier, relative, line in event_references:
        if is_aoe(identifier) and identifier not in definitions["event"]:
            findings["missing_references"].append((relative, line, f"event {identifier}"))
    for identifier, relative, line in focus_references:
        if is_aoe(identifier) and identifier not in definitions["focus"]:
            findings["missing_references"].append((relative, line, f"focus {identifier}"))
    for identifier, relative, line in focus_position_references:
        if is_aoe(identifier) and identifier not in definitions["focus"]:
            findings["missing_references"].append(
                (relative, line, f"relative-position focus {identifier}")
            )
    for identifier, relative, line in oob_references:
        if is_aoe(identifier) and not (root / "history" / "units" / f"{identifier}.txt").exists():
            findings["missing_references"].append((relative, line, f"OOB {identifier}"))
    for loc_key, relative, line in event_text + decision_names:
        if is_aoe(loc_key) and loc_key not in localisation:
            findings["missing_localisation"].append((relative, line, loc_key))
    for loc_key, relative, line in localisation_requirements:
        if loc_key not in localisation:
            findings["missing_localisation"].append((relative, line, loc_key))

    for loc_key, sites in localisation.items():
        if is_aoe(loc_key) and len(sites) > 1:
            findings["duplicate_localisation"].append((loc_key, sites))
    for province, sites in state_provinces.items():
        if len(sites) > 1:
            findings["map"].append((province, "duplicate state province", sites))
        if province not in region_provinces:
            findings["map"].append((province, "province has no strategic region", sites))
    for province, sites in region_provinces.items():
        if len(sites) > 1:
            findings["map"].append((province, "duplicate strategic-region province", sites))

    ownership_contract = {
        "ARG": {279, 300, 301, 506, 507, 688, 954, 1059, 1060, 1062, 1063, 1064, 1074, 1077},
        "PRU": {302, 305, 306, 307, 486, 487, 488, 489, 493, 649, 948, 1051, 1073},
    }
    state_files = {}
    for path in (root / "history" / "states").glob("*.txt"):
        match = re.match(r"(\d+)", path.name)
        if match:
            state_files[int(match.group(1))] = path
    for owner, state_ids in ownership_contract.items():
        for state_id in sorted(state_ids):
            path = state_files.get(state_id)
            if not path:
                findings["scenario_contract"].append((state_id, "state file missing"))
                continue
            text = path.read_text(encoding="utf-8-sig", errors="replace")
            actual = re.search(r"(?m)^\s*owner\s*=\s*(\w+)", text)
            cores = set(re.findall(r"(?m)^\s*add_core_of\s*=\s*(\w+)", text))
            if not actual or actual.group(1) != owner or not {owner, "SPR"}.issubset(cores):
                findings["scenario_contract"].append(
                    (state_id, f"expected owner {owner} and cores {owner},SPR")
                )

    report = {
        "root": str(root),
        "parsed_files": len(parsed),
        "definition_counts": {kind: len(values) for kind, values in definitions.items()},
        "findings": dict(findings),
    }
    if args.json:
        args.json.write_text(json.dumps(report, indent=2), encoding="utf-8")

    total = sum(len(items) for items in findings.values())
    print(f"Parsed {len(parsed)} script files.")
    if total:
        for category, items in sorted(findings.items()):
            if not items:
                continue
            print(f"\n{category}: {len(items)}")
            for item in items[:20]:
                print(f"  {item}")
            if len(items) > 20:
                print(f"  ... {len(items) - 20} more")
        print(f"\nFAILED: {total} proven finding(s).")
        return 1
    print("PASS: no proven structural, AOE-reference, localisation, map, or scenario-contract findings.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
