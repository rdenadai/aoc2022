import os
from functools import wraps
from os.path import abspath, dirname
from time import perf_counter
from typing import Any, Callable, List, Optional, Tuple

import httpx


class InputDownloader:
    def __init__(self, day: int, year: int = 2022) -> None:
        self.day = day
        self.year = year

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        filename = f"app/day{self.day:02}/input.txt"
        if os.path.exists(filename):
            return
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self._download())

    def _get_token(self) -> str:
        root_dir = dirname(abspath(__file__))
        token: str = "session="
        with open(f"{root_dir}/../../.env", "r", encoding="utf-8") as file:
            token = file.read().strip()
        return token

    def _download(self) -> str:
        with httpx.Client() as client:
            headers = {"Cookie": self._get_token()}
            req = client.get(
                f"https://adventofcode.com/{self.year}/day/{self.day}/input",
                follow_redirects=True,
                headers=headers,
            )
            if req.status_code == 200:
                return req.text
        return ""


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
        print(f"Elapsed time: {perf_counter() - start:.2f} seconds")
        return result

    return wrapped
