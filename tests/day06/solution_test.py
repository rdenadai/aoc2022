import pytest

from app.day06.parts import compute_part_1, compute_part_2


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
            7,
        ),
        (
            "bvwbjplbgvbhsrlpgdmjqwftvncz",
            5,
        ),
        (
            "nppdvjthqldpwncqszvftbrmjlhg",
            6,
        ),
        (
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
            10,
        ),
        (
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
            11,
        ),
    ],
)
def test_part_1(input_, expected):
    assert compute_part_1(input_) == expected


@pytest.mark.parametrize(
    "input_, expected",
    [
        (
            "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
            19,
        ),
        (
            "bvwbjplbgvbhsrlpgdmjqwftvncz",
            23,
        ),
        (
            "nppdvjthqldpwncqszvftbrmjlhg",
            23,
        ),
        (
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
            29,
        ),
        (
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
            26,
        ),
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
