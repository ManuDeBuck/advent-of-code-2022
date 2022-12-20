import re


def get_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def solve_1(input):
    dir_to_co = {
        "L": (0, -1),
        "R": (0, +1),
        "U": (1, 0),
        "D": (-1, 0)
    }

    xh, yh = (0, 0)
    xt, yt = (0, 0)
    tail_coordinates = set()

    command = input.pop(0)
    while command is not None:
        direction, am = re.match(r"^(.) ([0-9]+)$", command).groups()

        for _ in range(int(am)):
            delta = dir_to_co[direction]
            xh, yh = (xh + delta[0], yh + delta[1])
            if xh == xt and get_manhattan_distance(xh, yh, xt, yt) > 1:
                if direction == "R":
                    yt += 1
                else:
                    yt -= 1
            elif yh == yt and get_manhattan_distance(xh, yh, xt, yt) > 1:
                if direction == "U":
                    xt += 1
                else:
                    xt -= 1
            elif get_manhattan_distance(xh, yh, xt, yt) > 2:
                # need to make diagonal movement
                for opt in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
                    x_temp, y_temp = (xt + opt[0], yt + opt[1])
                    if get_manhattan_distance(xh, yh, x_temp, y_temp) <= 2:
                        xt, yt = x_temp, y_temp
                        break
            tail_coordinates.add((xt, yt))
        if len(input):
            command = input.pop(0)
        else:
            command = None

    return len(list(tail_coordinates))


def solve_2(input):
    pass


if __name__ == "__main__":
    day = "d9"
    with open(f"../inputs/{day}/input_simple.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
    with open(f"../inputs/{day}/input.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
