import pytest

from app.day07.parts import compute_part_1, compute_part_2

INPUT_TEXT = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


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
            95437,
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
            24933642,
        ),
    ],
)
def test_part_2(input_, expected):
    assert compute_part_2(input_) == expected
