import math
import re


def solve_1(input):
    # preprocess staple array
    crates = []
    line = input.pop(0)
    while len(line) > 0:
        crates.append(re.sub(" {2}", " ", re.sub(r"[\[\]]|", "", line)))
        line = input.pop(0)
    crates.pop()  # hacky way to remove last line

    # create staples 2D array
    nr_staples = math.ceil(len(crates[0]) / 2)
    staples = [[] for _ in range(nr_staples)]
    for crate_line in crates:
        for i in range(0, len(crate_line), 2):
            if crate_line[i] != " ":
                staples[i // 2].append(crate_line[i])

    # perform commands
    for command in input:
        staple_amount, staple_from, staple_to = map(int,
                                                    list(re.search(r"^[^0-9]*([0-9]+)[^0-9]*([0-9]+)[^0-9]*([0-9]+)$",
                                                                   command).groups()))
        staples[staple_to - 1] = staples[staple_from - 1][:staple_amount][::-1] + staples[staple_to - 1]
        staples[staple_from - 1] = staples[staple_from - 1][staple_amount:]

    return "".join([staple[0] if len(staple) else " " for staple in staples])


def solve_2(input):
    pass


if __name__ == "__main__":
    day = "d5"
    with open(f"../inputs/{day}/input_simple.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
    with open(f"../inputs/{day}/input.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
