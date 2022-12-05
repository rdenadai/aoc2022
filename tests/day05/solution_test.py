import pytest

from app.day05.parts import compute_part_1, compute_part_2

INPUT_TXT = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TXT,
            "CMZ",
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
            "MCD",
        )
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
