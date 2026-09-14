from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATE_DIR = ROOT / "history" / "states"

# State ownership approved for the 1936 Imperial World roster.
CORE_ASSIGNMENTS = {
    "AST": [285, 517, 518, 519, 520, 521, 522, 674, 870, 871, 872, 873],
    "NZL": [284],
    "SAF": [275, 681, 719, 940],
    "SAU": [292, 675, 678, 854, 857, 858, 859],
    "OMA": [679, 855, 856, 1022],  # OMA is the AOE Kingdom of Hejaz.
    "ENG": [294, 979, 1102, 1103],  # British Oman and Dhofar.
}

NON_CORE_ASSIGNMENTS = {
    "AST": [523, 725],  # New Guinea and Nauru.
    "NZL": [726],  # Samoa mandate.
}


def state_path(state_id: int) -> Path:
    matches = list(STATE_DIR.glob(f"{state_id}-*.txt"))
    if len(matches) != 1:
        raise RuntimeError(f"Expected one file for state {state_id}, found {matches}")
    return matches[0]


def rewrite_state(state_id: int, owner: str, core: bool) -> None:
    path = state_path(state_id)
    raw = path.read_bytes()
    has_bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    newline = "\r\n" if "\r\n" in text else "\n"
    owner_matches = list(re.finditer(r"(?m)^(?P<i>[ \t]*)owner\s*=\s*[A-Z0-9_]+[ \t]*(?=\r?$)", text))
    if len(owner_matches) != 1:
        raise RuntimeError(f"State {state_id}: expected one starting owner, found {len(owner_matches)}")

    match = owner_matches[0]
    indent = match.group("i")
    text = text[: match.start()] + f"{indent}owner = {owner}" + text[match.end() :]

    controller_pattern = re.compile(r"(?m)^(?P<i>[ \t]*)controller\s*=\s*[A-Z0-9_]+[ \t]*(?=\r?$)")
    text = controller_pattern.sub(lambda m: f"{m.group('i')}controller = {owner}", text)

    target_core_pattern = re.compile(
        rf"(?m)^[ \t]*add_core_of\s*=\s*{re.escape(owner)}[ \t]*\r?\n?"
    )
    has_target_core = target_core_pattern.search(text) is not None
    if core and not has_target_core:
        owner_line = re.search(
            rf"(?m)^(?P<i>[ \t]*)owner\s*=\s*{re.escape(owner)}[ \t]*\r?\n?", text
        )
        if owner_line is None:
            raise RuntimeError(f"State {state_id}: could not locate rewritten owner")
        insertion = f"{owner_line.group('i')}add_core_of = {owner}{newline}"
        text = text[: owner_line.end()] + insertion + text[owner_line.end() :]
    elif not core and has_target_core:
        text = target_core_pattern.sub("", text)

    encoded = text.encode("utf-8")
    if has_bom:
        encoded = b"\xef\xbb\xbf" + encoded
    path.write_bytes(encoded)
    print(f"{state_id}: owner={owner}, core={'yes' if core else 'no'}")


def main() -> None:
    seen: set[int] = set()
    for owner, state_ids in CORE_ASSIGNMENTS.items():
        for state_id in state_ids:
            if state_id in seen:
                raise RuntimeError(f"Duplicate assignment for state {state_id}")
            seen.add(state_id)
            rewrite_state(state_id, owner, core=True)
    for owner, state_ids in NON_CORE_ASSIGNMENTS.items():
        for state_id in state_ids:
            if state_id in seen:
                raise RuntimeError(f"Duplicate assignment for state {state_id}")
            seen.add(state_id)
            rewrite_state(state_id, owner, core=False)


if __name__ == "__main__":
    main()
