from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATE_DIR = ROOT / "history" / "states"

# State ownership approved for the 1936 Imperial World roster.
CORE_ASSIGNMENTS = {
    "AST": [285, 517, 518, 519, 520, 521, 522, 674, 870, 871, 872, 873],
    "NZL": [284, 723, 1136, 1139, 1140],
    "SAF": [275, 681, 719, 940],
    "SAU": [292, 675, 678, 854, 857, 858, 859],
    "OMA": [679, 855, 856, 1022],  # OMA is the AOE Kingdom of Hejaz.
    "ENG": [294, 979, 1102, 1103],  # British Oman and Dhofar.
    # Imperial administrations promoted to playable 1936 actors.
    "INS": [333, 334, 335, 446, 667, 668, 669, 672, 673, 974, 975, 976, 977, 978, 1014, 1126, 1127, 1128, 1135, 1137],
    "PHI": [327, 623, 624, 625, 626, 627, 628, 1108, 1109, 1110],
    "KOR": [525, 527],
    "BRM": [288, 640, 1018, 1019, 1020],
    "ALG": [459, 460, 513, 514, 933],
    "MOR": [461, 462],
    "TUN": [458, 665],
    "NFL": [331, 332],
    "NGA": [558, 900, 901, 902],
    "KEN": [546, 547, 548, 903, 904, 905],
    "SRL": [422],
    "COG": [295, 538, 718, 768, 769, 888, 889, 890],
    "LBA": [273, 448, 449, 450, 451, 661, 662, 663],
    "CUB": [315, 994],
    "AFG": [267, 1008, 1009, 1010],
    "AZR": [419, 988],
    "ANG": [540, 796, 891, 892],
    "MZB": [544, 896, 897],
    "ICE": [100, 1043],
    # Regional governments survive the opening Qing crisis as playable actors.
    "SIK": [287, 617, 618, 619, 759, 760, 1121],
    "TIB": [322, 601, 752, 757, 758],
    "YUN": [325, 747, 751],
    "XSM": [283, 604, 753, 754, 755, 756, 1119, 1122, 1123, 1124],
    "XIC": [744, 1111, 1125],
    "IAF": [550, 559],
}

NON_CORE_ASSIGNMENTS = {
    "AST": [523, 634, 725, 1096],  # New Guinea, Solomons, Nauru and Kaiser Wilhelmsland.
    "NZL": [726],  # Samoa mandate.
}

# Former British homeland/colonial cores must not survive the Dominion and
# independent-republic roster restoration. Ottoman cores remain as deliberate
# claims on the newly independent Arabian states.
REMOVE_CORES = {
    "ENG": {
        275, 284, 285, 517, 518, 519, 520, 521, 522, 523, 634, 674, 681,
        719, 723, 725, 726, 870, 871, 872, 873, 940, 1022, 1096, 1136, 1139,
        1140,
    },
    "JAP": {
        327, 333, 334, 335, 446, 525, 527, 623, 624, 625, 626, 627, 628,
        667, 668, 669, 672, 673, 974, 975, 976, 977, 978, 1014, 1108, 1109,
        1110, 1126, 1127, 1128, 1135, 1137,
    },
    "RAJ": {288, 640, 1018, 1019, 1020},
    "FRA": {458, 459, 460, 461, 462, 513, 514, 665, 933},
    "BEL": {295, 538, 718, 768, 769, 888, 889, 890},
    "ITA": {273, 448, 449, 450, 451, 550, 559, 661, 662, 663},
    "POR": {540, 544, 796, 891, 892, 896, 897},
    "GER": {100, 1043},
}


def state_path(state_id: int) -> Path:
    matches = [
        path
        for path in STATE_DIR.glob(f"{state_id}*.txt")
        if re.match(rf"^{state_id}(?:-|\s)", path.name)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one file for state {state_id}, found {matches}")
    text = matches[0].read_text(encoding="utf-8-sig", errors="replace")
    if re.search(rf"(?m)^\s*id\s*=\s*{state_id}\s*$", text) is None:
        raise RuntimeError(f"State id mismatch in {matches[0]}")
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

    for old_core, state_ids in REMOVE_CORES.items():
        if state_id not in state_ids:
            continue
        old_core_pattern = re.compile(
            rf"(?m)^[ \t]*add_core_of\s*=\s*{re.escape(old_core)}[ \t]*\r?\n?"
        )
        text = old_core_pattern.sub("", text)

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
