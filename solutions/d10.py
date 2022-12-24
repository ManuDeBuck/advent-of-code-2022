def solve_1(input):
    register = 1
    cycle = 1
    sum = 0
    cmd = input.pop(0)

    col = 0

    if cmd == "noop":
        remaining = 0
    else:
        remaining = 1

    while cmd is not None:
        if col in [register - 1, register, register + 1]:
            col += 1
            print("#", end="")
        else:
            col += 1
            print(".", end="")
        if col % 40 == 0:
            col = 0
            print("")

        if cycle in list(range(20, 221, 40)):
            sum += register * cycle

        cycle += 1

        if remaining == 0:
            if cmd != "noop":
                register += int(cmd[5:])

            if len(input):
                cmd = input.pop(0)
            else:
                cmd = None

            if cmd == "noop":
                remaining = 0
            else:
                remaining = 1
        else:
            remaining -= 1


    print("")
    return sum


if __name__ == "__main__":
    day = "d10"
    with open(f"../inputs/{day}/input_simple.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
    with open(f"../inputs/{day}/input.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
