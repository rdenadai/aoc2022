import pytest

from app.day02.parts import HANDS_MAP, compute_part_1, compute_part_2

INPUT_TXT = """
A Y
B X
C Z
"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TXT,
            15,
        )
    ],
)
def test_part_1(input_, expected):
    assert compute_part_1(input_) == expected


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TXT,
            12,
        )
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected


@pytest.mark.parametrize("input_, expected", [("A", "X"), ("B", "Y"), ("C", "Z")])
def test_hands_map(input_, expected):
    assert HANDS_MAP[input_] == HANDS_MAP[expected]
