import sys
from collections import defaultdict
from typing import Iterable, List, Tuple

from app.support.utils import main, parse_module_to_day, timing


def compute(s: str, size: int) -> int:
    i, k = 0, size
    for i, _ in enumerate(s):
        slice_ = s[i : i + size]
        if len(set(slice_)) == size:
            return s.index(slice_) + size
    return 0


@timing
def compute_part_1(s: str) -> str:
    return compute(s, 4)


@timing
def compute_part_2(s: str) -> str:
    return compute(s, 14)


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
