import sys
from collections import defaultdict
from typing import Iterable, List, Tuple

from app.support.utils import main, parse_module_to_day, timing


def _chunks(_list: List, n: int = 3) -> Iterable[List]:
    for i in range(0, len(_list), n):
        yield _list[i : i + n]


def _parser_input(s: str) -> Tuple[List, List[str]]:
    crates, moves = s.split("\n\n")

    crates = [line.strip().split() for line in filter(None, crates.replace("    ", " [] ").splitlines()[:-1])]
    d = defaultdict(list)
    for crate in crates:
        for i, c in enumerate(crate):
            d[i].append(c)
    for k, v in d.items():
        d[k] = list(filter(lambda s: s.replace("[]", ""), reversed(v)))
    crates = list(d.values())

    moves = list(_chunks([int(move) for move in moves.split() if move.isdigit()]))

    return crates, moves


@timing
def compute_part_1(s: str) -> str:
    crates, moves = _parser_input(s)
    for move in moves:
        for _ in range(move[0]):
            crates[move[2] - 1].append(crates[move[1] - 1].pop())
    return "".join([crate[-1] for crate in crates]).replace("[", "").replace("]", "")


@timing
def compute_part_2(s: str) -> str:
    crates, moves = _parser_input(s)
    for move in moves:
        sub_stack = reversed([crates[move[1] - 1].pop() for _ in range(move[0])])
        crates[move[2] - 1].extend(sub_stack)
    return "".join([crate[-1] for crate in crates]).replace("[", "").replace("]", "")


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
