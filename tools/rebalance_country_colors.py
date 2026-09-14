from __future__ import annotations

import colorsys
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COLOR_FILE = ROOT / "common" / "countries" / "colors.txt"

# Anchor colors give the 1936 powers and the new roster a deliberate identity.
ANCHORS = {
    "GER": (112, 116, 125),
    "ENG": (196, 76, 90),
    "SOV": (75, 145, 98),
    "SWE": (83, 143, 202),
    "FRA": (77, 118, 203),
    "BEL": (190, 155, 77),
    "HOL": (222, 132, 67),
    "POL": (220, 111, 139),
    "AUS": (225, 218, 211),
    "SPR": (210, 160, 73),
    "ITA": (78, 156, 101),
    "ROM": (206, 166, 78),
    "YUG": (103, 122, 181),
    "TUR": (151, 96, 73),
    "GRE": (96, 157, 214),
    "POR": (68, 146, 103),
    "AST": (102, 157, 203),
    "NZL": (117, 153, 187),
    "SAF": (181, 111, 52),
    "SAU": (198, 174, 112),
    "OMA": (151, 76, 78),
    "CHI": (192, 160, 78),
    "MAN": (218, 189, 92),
    "MON": (151, 105, 170),
    "SIK": (91, 157, 133),
    "XSM": (187, 135, 78),
    "TIB": (151, 126, 190),
    "YUN": (102, 164, 190),
    "XIC": (184, 105, 119),
}

TAG_START = re.compile(r"(?m)^(?P<tag>[A-Z0-9_]+)\s*=\s*\{")
RGB = re.compile(r"rgb\s*\{\s*(\d+)\s+(\d+)\s+(\d+)\s*\}")


def rebalance(rgb: tuple[int, int, int]) -> tuple[int, int, int]:
    r, g, b = (value / 255 for value in rgb)
    hue, lightness, saturation = colorsys.rgb_to_hls(r, g, b)
    if saturation < 0.12:
        lightness = min(0.82, max(0.42, lightness * 1.12 + 0.05))
        saturation = min(saturation, 0.08)
    else:
        lightness = min(0.72, max(0.42, lightness * 1.10 + 0.05))
        saturation = min(0.68, max(0.36, saturation * 0.95))
    converted = colorsys.hls_to_rgb(hue, lightness, saturation)
    return tuple(round(value * 255) for value in converted)


def main() -> None:
    raw = COLOR_FILE.read_bytes()
    has_bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    newline = "\r\n" if "\r\n" in text else "\n"
    matches = list(TAG_START.finditer(text))
    if len(matches) < 100:
        raise RuntimeError(f"Unexpectedly small country palette: {len(matches)} blocks")

    output: list[str] = [text[: matches[0].start()]]
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start() : end]
        tag = match.group("tag")
        values = RGB.findall(block)
        if not values:
            output.append(block)
            continue
        source = tuple(int(value) for value in values[0])
        target = ANCHORS.get(tag, rebalance(source))
        replacement = f"rgb {{ {target[0]} {target[1]} {target[2]} }}"
        block = RGB.sub(replacement, block)
        output.append(block)

    result = newline.join(line.rstrip() for line in "".join(output).splitlines()) + newline
    encoded = result.encode("utf-8")
    if has_bom:
        encoded = b"\xef\xbb\xbf" + encoded
    COLOR_FILE.write_bytes(encoded)
    print(f"Rebalanced {len(matches)} country-color blocks with {len(ANCHORS)} anchors")


if __name__ == "__main__":
    main()
