import sys
from enum import IntEnum

from app.support.utils import main, parse_module_to_day, timing


class Outcome(IntEnum):
    LOOSE = 0
    DRAW = 3
    WON = 6


class Game(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Game) and self.value == __o.value

    def __gt__(self, __o: object) -> bool:
        if isinstance(__o, Game) and (
            (self == Game.ROCK and __o == Game.SCISSOR)
            or (self == Game.SCISSOR and __o == Game.PAPER)
            or (self == Game.PAPER and __o == Game.ROCK)
        ):
            return True
        return False

    def __lt__(self, __o: object) -> bool:
        if isinstance(__o, Game) and (
            (self == Game.SCISSOR and __o == Game.ROCK)
            or (self == Game.PAPER and __o == Game.SCISSOR)
            or (self == Game.ROCK and __o == Game.PAPER)
        ):
            return True
        return False

    def __hash__(self) -> int:
        return self.name.__hash__()


HANDS_MAP = {
    "A": Game.ROCK,
    "B": Game.PAPER,
    "C": Game.SCISSOR,
    "X": Game.ROCK,
    "Y": Game.PAPER,
    "Z": Game.SCISSOR,
}


HANDS_MAP_REVERSE = {
    "won": {
        Game.ROCK: Game.PAPER,
        Game.PAPER: Game.SCISSOR,
        Game.SCISSOR: Game.ROCK,
    },
    "loose": {
        Game.ROCK: Game.SCISSOR,
        Game.PAPER: Game.ROCK,
        Game.SCISSOR: Game.PAPER,
    },
}


@timing
def compute_part_1(s: str) -> int:
    total = 0
    hands = HANDS_MAP
    for line in filter(None, s.splitlines()):
        p1, p2 = line.split()
        h1, h2 = hands[p1], hands[p2]
        if h2 > h1:
            total += h2 + Outcome.WON
        elif h2 < h1:
            total += h2 + Outcome.LOOSE
        else:
            total += h2 + Outcome.DRAW
    return total


@timing
def compute_part_2(s: str) -> int:
    total = 0
    hands, reversed_hands = HANDS_MAP, HANDS_MAP_REVERSE
    for line in filter(None, s.splitlines()):
        p1, p2 = line.split()
        hand = hands[p1]
        if p2 == "X":
            total += reversed_hands["loose"][hand] + Outcome.LOOSE
        elif p2 == "Y":
            total += hand + Outcome.DRAW
        elif p2 == "Z":
            total += reversed_hands["won"][hand] + Outcome.WON
    return total


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
