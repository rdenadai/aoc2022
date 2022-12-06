# Some regex parts taken from: https://github.com/anthonywritescode/aoc2022 (MIT License)

import os
import re
from functools import wraps
from os.path import abspath, dirname
from time import perf_counter
from typing import Any, Callable, List, Optional, Tuple

import httpx

TOO_QUICK = re.compile("You gave an answer too recently.*to wait.")
WRONG = re.compile(r"That's not the right answer.*?\.")
RIGHT = "That's the right answer!"
ALREADY_DONE = re.compile(r"You don't seem to be solving.*\?")


def _get_token() -> str:
    root_dir = dirname(abspath(__file__))
    token: str = "session="
    with open(f"{root_dir}/../../.env", "r", encoding="utf-8") as file:
        token = file.read().strip()
    return token


class InputDownload:
    def __init__(self, day: int, year: int = 2022) -> None:
        self.day = day
        self.year = year

    def download(self) -> str:
        filename = f"app/day{self.day:02}/input.txt"
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                return file.read()
        contents: str = self._download_input_data()
        with open(filename, "w", encoding="utf-8") as file:
            file.write(contents)
        return contents

    def _download_input_data(self) -> str:
        with httpx.Client() as client:
            headers = {"Cookie": _get_token()}
            req = client.get(
                f"https://adventofcode.com/{self.year}/day/{self.day}/input",
                follow_redirects=True,
                headers=headers,
            )
            if req.status_code == 200:
                return req.text
        return ""


class InputSubmit:
    def __init__(self, day: int, year: int = 2022) -> None:
        self.day = day
        self.year = year

    def submit(self, part: int, answer: str):
        filename = f"app/day{self.day:02}/.submit_part_{part}.txt"
        if os.path.exists(filename):
            return "Already submitted"

        with httpx.Client() as client:
            headers = {"Cookie": _get_token()}
            req = client.post(
                f"https://adventofcode.com/{self.year}/day/{self.day}/answer",
                data={"level": part, "answer": answer},
                follow_redirects=True,
                headers=headers,
            )
            correct, text = self._parse_answer(req.text)

        if correct:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(f"Part {part} answer: {answer}")

        return text

    def _parse_answer(self, contents: str) -> Tuple[bool, str]:
        for error_regex in (WRONG, TOO_QUICK):
            error_match = error_regex.search(contents)
            if error_match:
                return False, error_match[0]
        error_match = ALREADY_DONE.search(contents)
        if error_match:
            return True, error_match[0]
        if RIGHT in contents:
            return True, RIGHT
        return False, "Unknown error"


def main(day, module, compute_part_1, compute_part_2) -> int:
    input_submit: InputSubmit = InputSubmit(day=day)
    contents: str = InputDownload(day=day).download()
    print("-" * 20)
    answer_part_1 = compute_part_1(contents)
    print("Part 1 answer: ", answer_part_1)
    print(input_submit.submit(part=1, answer=str(answer_part_1)))
    print("-" * 20)
    answer_part_2 = compute_part_2(contents)
    print("Part 2 answer: ", answer_part_2)
    print(input_submit.submit(part=2, answer=str(answer_part_2)))
    return 0


def parse_module_to_day(module_name: str = "") -> Tuple[str, int]:
    module_name = "app.day01" if not module_name or not isinstance(module_name, str) else module_name
    splitted: Optional[List] = module_name.split(".")
    if splitted:
        try:
            module, sday = splitted[-1], splitted[-1]
            return module, int(sday.replace("day", ""))
        except ValueError:
            ...
    return "day01", 1


def timing(_func: Callable):
    @wraps(_func)
    def wrapped(*args, **kwargs) -> Callable:
        start = perf_counter()
        result = _func(*args, **kwargs)
        print(f"Elapsed time: {perf_counter() - start:.5f} seconds")
        return result

    return wrapped
