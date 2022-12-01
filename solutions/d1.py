import numpy as np


def compute_sums(input):
    elves = []
    line = input.pop()
    elf_sum = 0
    while line is not None:
        if len(line) == 0:
            elves.append(elf_sum)
            elf_sum = 0
        else:
            elf_sum += int(line)

        if len(input):
            line = input.pop()
        else:
            line = None
    return elves


def solve_1(input):
    return np.max(compute_sums(input))


def solve_2(input):
    elves = compute_sums(input)
    return np.sum(np.sort(elves)[::-1][:3])


if __name__ == "__main__":
    day = "d1"
    with open(f"../inputs/{day}/input_simple.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
    with open(f"../inputs/{day}/input.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
