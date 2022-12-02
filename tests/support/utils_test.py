import pytest

from app.support.utils import parse_module_to_day


@pytest.mark.parametrize(
    "input_, expected",
    [
        ("app.day01", ("day01", 1)),
        ("app.day02", ("day02", 2)),
        ("app.day10", ("day10", 10)),
        ("app.day25", ("day25", 25)),
        ("app", ("day01", 1)),
        ("", ("day01", 1)),
        (None, ("day01", 1)),
        (1, ("day01", 1)),
        (False, ("day01", 1)),
    ],
)
def test_parse_module_to_day(input_, expected):
    assert parse_module_to_day(input_) == expected
