import sys
from collections import defaultdict
from math import sqrt
from typing import DefaultDict, Set, Tuple

from app.support.utils import main, parse_module_to_day, timing


def euclidian_distance(
    point1: Tuple[int, int],
    point2: Tuple[int, int],
) -> float:
    """Return True if points are in the same line or column (using Euclidian distance)"""
    x1, y1 = point1
    x2, y2 = point2
    return round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)


def is_p1_close_p2(
    point1: Tuple[int, int],
    point2: Tuple[int, int],
):
    distance = euclidian_distance(point1, point2)
    return distance <= 1.41 or round(distance, 2) == 1.0, distance


def _parser_input(s: str, n_tails=1) -> DefaultDict[Tuple, Set]:
    marker_positions: DefaultDict[Tuple, Set] = defaultdict(set)
    # Initial position
    marker_positions[(0, 0)] = set("H")
    for i in range(n_tails):
        marker_positions[(0, 0)].add(f"T{i+1}")
    # Reference position
    head, tails = (0, 0), list((0, 0) for _ in range(n_tails))
    for line in s.splitlines():
        pos, sqtd = line.split()
        qtd = int(sqtd)
        for _ in range(1, qtd + 1):
            # Head movement
            old_head = head
            if pos == "R":  # right
                head = (head[0] + 1, head[1])
            elif pos == "L":  # left
                head = (head[0] - 1, head[1])
            elif pos == "U":  # up
                head = (head[0], head[1] + 1)
            elif pos == "D":  # down
                head = (head[0], head[1] - 1)
            marker_positions[head].add("H")
            # Tail movement
            new_head = head
            for i, tail in enumerate(tails):
                n_tail = tail
                is_close, _ = is_p1_close_p2(new_head, tail)
                if not is_close:
                    # Part 2 isn't correct!
                    n_tail = (old_head[0], old_head[1])
                old_head = tails[i]
                new_head = n_tail
                # Update tail position
                tails[i] = n_tail
                # Add tail has passed to this position
                marker_positions[n_tail].add(f"T{i+1}")
    return marker_positions


@timing
def compute_part_1(s: str, n_tails=1) -> int:
    if not s or not isinstance(s, str):
        return 0
    marker_positions = _parser_input(s, n_tails=1)
    return sum(1 for val in marker_positions.values() if "T1" in val)


@timing
def compute_part_2(s: str) -> int:
    if not s or not isinstance(s, str):
        return 0
    marker_positions = _parser_input(s, n_tails=9)
    return sum(1 for val in marker_positions.values() if "T9" in val)


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
