import sys

from app.support.utils import main, parse_module_to_day, timing


def compute(s: str, size: int) -> int:
    """
    # Not compact, but easier to 'understand' ... and faster (don't need to run through the whole list)
    for i, _ in enumerate(s):
        if len(set(s[i : i + size])) == size:
            return i + size
    """
    if not s:
        return 0
    (total, *_) = (i + size for i, _ in enumerate(s) if len(set(s[i : i + size])) == size)
    return total


@timing
def compute_part_1(s: str) -> str:
    return compute(s, 4)


@timing
def compute_part_2(s: str) -> str:
    return compute(s, 14)


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
