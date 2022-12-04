import pytest

from app.day04.parts import compute_part_1, compute_part_2

INPUT_TXT = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TXT,
            2,
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
            4,
        )
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
