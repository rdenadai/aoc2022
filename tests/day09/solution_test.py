import pytest

from app.day09.parts import compute_part_1, compute_part_2

INPUT_TEXT_1 = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

INPUT_TEXT_2 = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            "",
            0,
        ),
        (
            None,
            0,
        ),
        (
            INPUT_TEXT_1,
            13,
        ),
    ],
)
def test_part_1(input_, expected):
    assert compute_part_1(input_) == expected


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            "",
            0,
        ),
        (
            None,
            0,
        ),
        (
            INPUT_TEXT_2,
            36,
        ),
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
