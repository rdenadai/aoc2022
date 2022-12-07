import pytest

from app.day00.parts import compute_part_1, compute_part_2

INPUT_TEXT = """\

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
            0,
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
            0,
        ),
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
