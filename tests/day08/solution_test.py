import pytest

from app.day08.parts import compute_part_1, compute_part_2

INPUT_TEXT = """\
30373
25512
65332
33549
35390
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
            INPUT_TEXT,
            21,
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
            INPUT_TEXT,
            8,
        ),
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
