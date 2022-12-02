def try_play(p1, p2):
    if p1 == p2:
        return 3
    if p1 == 1 and p2 == 2:  # paper wins over rock
        return 6
    if p1 == 2 and p2 == 3:  # scissors wins over paper
        return 6
    if p1 == 3 and p2 == 1:  # rock wins over scissors
        return 6
    return 0


def get_score(elf, self):
    return self + try_play(elf, self)


def solve_1(input):
    mapper = {
        "A": 1,  # rock
        "B": 2,  # paper
        "C": 3,  # scissors
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    sum = 0
    for line in input:
        elf = mapper[line[0]]
        self = mapper[line[2]]
        sum += get_score(elf, self)
    return sum


def solve_2(input):
    mapper = {
        "A": 1,  # rock
        "B": 2,  # paper
        "C": 3,  # scissors
        "X": 0,  # lose
        "Y": 3,  # draw
        "Z": 6  # win
    }
    sum = 0
    for line in input:
        elf = mapper[line[0]]
        result = mapper[line[2]]
        for play in [1, 2, 3]:
            if try_play(elf, play) == result:
                sum += get_score(elf, play)
    return sum


if __name__ == "__main__":
    day = "d2"
    with open(f"../inputs/{day}/input_simple.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
    with open(f"../inputs/{day}/input.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
