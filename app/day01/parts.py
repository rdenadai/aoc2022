import sys
from collections import defaultdict
from typing import DefaultDict

from app.support.utils import main, parse_module_to_day, timing


def _compute(s: str) -> DefaultDict[int, int]:
    elves: DefaultDict[int, int] = defaultdict(int)
    i = 1
    for line in s.splitlines():
        if line:
            elves[i] += int(line)
        else:
            i += 1
    return elves


@timing
def compute_part_1(s: str) -> int:
    elves: DefaultDict[int, int] = _compute(s)
    return max(elves.values())


@timing
def compute_part_2(s: str) -> int:
    elves: DefaultDict[int, int] = _compute(s)
    return sum(sorted(elves.values(), reverse=True)[:3])


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
