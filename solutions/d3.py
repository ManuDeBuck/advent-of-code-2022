import string

ALPHABET_VALUES = list(string.ascii_letters)


def solve_1(input):
    priorities = 0
    for line in input:
        h1 = set(line[:len(line) // 2])
        h2 = set(line[len(line) // 2:])
        common = list(h1.intersection(h2))[0]
        priorities += ALPHABET_VALUES.index(common) + 1
    return priorities


def solve_2(input):
    priorities = 0
    for i in range(0, len(input), 3):
        h1 = set(input[i])
        h2 = set(input[i + 1])
        h3 = set(input[i + 2])
        common = list(h1.intersection(h2).intersection(h3))[0]
        priorities += ALPHABET_VALUES.index(common) + 1
    return priorities


if __name__ == "__main__":
    day = "d3"
    with open(f"../inputs/{day}/input_simple.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
    with open(f"../inputs/{day}/input.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
