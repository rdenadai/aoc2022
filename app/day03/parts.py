import sys
from string import ascii_lowercase, ascii_uppercase

from app.support.utils import InputDownloader, parse_module_to_day, timing

POINTS = dict(zip(ascii_lowercase, range(1, 27))) | dict(zip(ascii_uppercase, range(27, 53)))


@timing
def compute_part_1(s: str) -> int:
    total, points = 0, POINTS
    for line in filter(None, s.splitlines()):
        split_pos = len(line) // 2
        first_half, sec_half = list(line[:split_pos]), list(line[split_pos:])
        common = set(first_half) & set(sec_half)
        total += sum(points[c] for c in common)
    return total


@timing
def compute_part_2(s: str) -> int:
    total, points = 0, POINTS
    lines = list(filter(None, s.splitlines()))
    while lines:
        i1, i2, i3 = lines[:3]
        common = set(i1) & set(i2) & set(i3)
        total += sum(points[c] for c in common)
        lines = lines[3:]
    return total


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    InputDownloader(day=day)()
    with open(f"app/{module}/input.txt", "r") as file:
        contents = file.read()
        print("-" * 20)
        print("Part 1 answer: ", compute_part_1(contents.strip()))
        print("-" * 20)
        print("Part 2 answer: ", compute_part_2(contents.strip()))