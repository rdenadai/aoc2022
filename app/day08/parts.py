import sys
from functools import reduce
from typing import List, Tuple

from app.support.utils import main, parse_module_to_day, timing


def _parser_input(s: str) -> Tuple[int, int, List]:
    matrix: List = [list(map(int, line)) for line in s.splitlines()]

    w, h = len(matrix[0]), len(matrix)
    return (
        w,
        h,
        [
            (
                matrix[i][k + 1],  # tree height
                (
                    list(reversed([matrix[j][k + 1] for j in range(0, i)])),  # up
                    list(reversed(matrix[i][: k + 1])),  # left
                    [matrix[j][k + 1] for j in range(i + 1, h)],  # down
                    matrix[i][k + 2 :],  # right
                ),
            )
            for i in range(1, h - 1)
            for k in range(0, w - 2)
        ],
    )


@timing
def compute_part_1(s: str) -> int:
    if not s or not isinstance(s, str):
        return 0

    w, h, matrix = _parser_input(s)

    total_visible = 0
    for block in matrix:
        is_visible = False
        tree_height, position = block
        is_visible = any(all(tree_height > item for item in values) for values in position)
        total_visible += is_visible

    return (w * 2 + (h - 2) * 2) + total_visible


@timing
def compute_part_2(s: str) -> int:
    if not s or not isinstance(s, str):
        return 0
    w, h, matrix = _parser_input(s)

    acc = 0
    for block in matrix:
        total = 1
        tree_height, position = block
        for values in position:
            qtd = 0
            for tree in values:
                qtd += 1
                if tree >= tree_height:
                    break
            total *= qtd
        acc = total if total > acc else acc
    return acc


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
