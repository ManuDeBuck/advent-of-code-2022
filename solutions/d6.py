def solve(input, length):
    line = input.pop()
    for i in range(len(line) - length):
        if len(set(line[i:i + length])) == length:
            return i + length


def solve_1(input):
    return solve(input, 4)


def solve_2(input):
    return solve(input, 14)


if __name__ == "__main__":
    day = "d6"
    with open(f"../inputs/{day}/input_simple.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
    with open(f"../inputs/{day}/input.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
