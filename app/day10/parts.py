import sys
from collections import defaultdict

from app.support.utils import main, parse_module_to_day, timing

# Show Letters ...
# from matplotlib import pyplot as plt


@timing
def compute_part_1(s: str) -> int:
    if not s or not isinstance(s, str):
        return 0
    rcycles, register_x = 0, 1
    signal = defaultdict(int)
    for line in s.splitlines():
        rcycles += 2 if line.startswith("addx") else 1
        size = rcycles / 20
        if round(size - int(size), 2) <= 0.05:
            cycles = int(size) * 20
            if cycles not in signal:
                signal[cycles] = register_x * cycles
        if line.startswith("addx"):
            _, number = line.split()
            register_x += int(number)
    return sum(signal.get(i, 0) for i in (20, 60, 100, 140, 180, 220))


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def draw_sprint(register_x):
    if register_x >= 0:
        return "".join("." for _ in range(register_x - 1)) + "###" + "".join("." for _ in range(40 - (register_x + 2)))
    m = "###"[:register_x]
    return m + "".join(["." for _ in range(40 - (register_x + len(m) - 1))])


@timing
def compute_part_2(s: str) -> str:
    if not s or not isinstance(s, str):
        return ""
    sprite = "###" + "." * 37
    crt, register_x, needle = [], 1, 0
    for line in s.splitlines():
        cycle, addx = 1, 0
        if line.startswith("addx"):
            cycle = 2
            addx = int(line.split()[-1])
        for _ in range(cycle):
            crt.append(sprite[needle])
            needle += 1
            needle = 0 if needle == 40 else needle
        register_x += addx
        sprite = draw_sprint(register_x)
    # Show letters ...
    # plt.imshow([m for m in chunks([1 if i == "#" else 0 for i in crt], 40)])
    # plt.show()
    return "\n".join("".join(i) for i in chunks(crt, 40))


if __name__ == "__main__":  # pragma: no cover
    module, day = parse_module_to_day(sys.modules[__name__].__package__)

    main(day, module, compute_part_1, compute_part_2)
