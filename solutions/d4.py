import re


def solve_1(input):
    count = 0
    for line in input:
        l1, h1, l2, h2 = map(int, list(re.search(r"^([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)$", line).groups()))
        if l1 <= l2 and h2 <= h1 or l2 <= l1 and h1 <= h2:
            count += 1
    return count


def solve_2(input):
    count = 0
    for line in input:
        l1, h1, l2, h2 = map(int, list(re.search(r"^([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)$", line).groups()))
        if not(h1 < l2 or h2 < l1):
            count += 1
    return count


if __name__ == "__main__":
    day = "d4"
    with open(f"../inputs/{day}/input_simple.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
    with open(f"../inputs/{day}/input.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
