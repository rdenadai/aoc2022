import pytest

from app.day01.parts import compute_part_1, compute_part_2

INPUT_TXT = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            INPUT_TXT,
            24000,
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
            45000,
        )
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
