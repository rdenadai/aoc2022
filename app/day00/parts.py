import sys

from app.support.utils import main, parse_module_to_day, timing


@timing
def compute_part_1(s: str) -> int:
    if not s or not isinstance(s, str):
        return 0
    # Calculate response
    return 0


@timing
def compute_part_2(s: str) -> int:
    if not s or not isinstance(s, str):
        return 0
    # Calculate response
    return 0


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
