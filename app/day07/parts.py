from __future__ import annotations

import sys
from dataclasses import dataclass, field
from typing import Iterable, List, Optional

from app.support.utils import main, parse_module_to_day, timing

# in case you need files:
# @dataclass(eq=False, slots=True)
# class File:
#     name: str
#     size: int = 0


@dataclass(eq=False, slots=True)
class Node:
    path: str
    size_bytes: int = 0  # in bytes ?
    # in case you need files:
    # files: List[Optional[File]] = field(default_factory=list)
    parent: Optional[Node] = None
    children: List[Node] = field(default_factory=list)


def get_children_part_1(node: Node) -> Iterable[int]:
    if node.size_bytes < 100_000:
        yield node.size_bytes
    for child in node.children:
        yield sum(get_children_part_1(child))


def get_children_part_2(node: Node) -> Iterable[int]:
    yield node.size_bytes
    for child in node.children:
        yield from get_children_part_2(child)


def sum_bytes_to_parents(node: Node, bytes_: int) -> None:
    if node.parent:
        node.parent.size_bytes += bytes_
        sum_bytes_to_parents(node.parent, bytes_)


def parse_input(s: str) -> Node:
    root = ref = Node(path="/")
    for line in s.splitlines():
        if line.startswith("$ ls"):
            continue
        tokens = line.split()
        if line.startswith("$ cd") and line not in ("$ cd /", "$ cd .."):  # Down one lvl
            cur = Node(path=tokens[-1], parent=ref)
            ref.children.append(cur)
            ref = cur
        elif line == "$ cd ..":  # up one lvl
            ref = ref.parent
        elif len(tokens) >= 2 and tokens[0].isdigit():  # file
            bytes_: int = int(tokens[0])
            ref.size_bytes += bytes_
            # in case you need files:
            # ref.files.append(File(tokens[1].strip(), bytes_))
            sum_bytes_to_parents(ref, bytes_)
    return root


@timing
def compute_part_1(s: str) -> int:
    if not s or not isinstance(s, str):
        return 0
    root = parse_input(s)
    # Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
    return sum(item for item in get_children_part_1(root))


@timing
def compute_part_2(s: str) -> int:
    if not s or not isinstance(s, str):
        return 0
    root = parse_input(s)
    # Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update.
    traverse = get_children_part_2(root)
    root_dir: int = next(traverse)
    min_bytes_to_release: int = 30_000_000 - (70_000_000 - root_dir)
    return min(item for item in traverse if item >= min_bytes_to_release)


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
