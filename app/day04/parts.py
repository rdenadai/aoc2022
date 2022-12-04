import sys
from typing import List, Tuple

from app.support.utils import InputDownloader, InputSubmit, parse_module_to_day, timing


def _parse_line(line: str) -> Tuple[int, ...]:
    pairs = line.split(",")
    p1, p2 = pairs[0].split("-"), pairs[1].split("-")
    a1, b1, a2, b2 = int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1])
    return a1, b1, a2, b2


@timing
def compute_part_1(s: str) -> int:
    total = 0
    for line in filter(None, s.splitlines()):
        a1, b1, a2, b2 = _parse_line(line)
        if (a1 >= a2 and b1 <= b2) or (a2 >= a1 and b2 <= b1):
            total += 1
    return total


@timing
def compute_part_2(s: str) -> int:
    total = 0
    for line in filter(None, s.splitlines()):
        a1, b1, a2, b2 = _parse_line(line)
        if (a1 <= a2 <= b1) or (a2 <= a1 <= b2):
            total += 1
    return total


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    InputDownloader(day=day)()
    input_submit: InputSubmit = InputSubmit(day=day)
    with open(f"app/{module}/input.txt", "r") as file:
        contents = file.read()
        print("-" * 20)
        answer_part_1 = compute_part_1(contents.strip())
        print("Part 1 answer: ", answer_part_1)
        print(input_submit.submit(part=1, answer=str(answer_part_1)))
        print("-" * 20)
        answer_part_2 = compute_part_2(contents.strip())
        print("Part 2 answer: ", answer_part_2)
        print(input_submit.submit(part=2, answer=str(answer_part_2)))
