def solve_1(input):
    def get_column(j):
        c = []
        for i, el in enumerate(grid):
            c.append(el[j])
        return c

    def collect_path_max(i, j):
        l = grid[i][:j]
        r = grid[i][j + 1:]
        col = get_column(j)
        t = col[:i]
        b = col[i + 1:]
        return [max(l), max(r), max(t), max(b)]

    grid = [[int(el) for el in line] for line in input]
    count = 0
    for i, row in enumerate(grid):
        for j, el in enumerate(row):
            if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
                count += 1
            elif min(collect_path_max(i, j)) < el:
                count += 1
    return count


def solve_2(input):
    def get_column(j):
        c = []
        for i, el in enumerate(grid):
            c.append(el[j])
        return c

    def scenic_score(i, j):
        def c(a):
            count = 0
            for val in a:
                if val < el:
                    count += 1
                else:
                    count += 1
                    break
            return count
        l = grid[i][:j]
        r = grid[i][j + 1:]
        col = get_column(j)
        t = col[:i]
        b = col[i + 1:]
        return c(l[::-1]) * c(r) * c(t[::-1]) * c(b)

    grid = [[int(el) for el in line] for line in input]
    max_ss = 0
    for i, row in enumerate(grid):
        for j, el in enumerate(row):
            ss = scenic_score(i, j)
            if ss > max_ss:
                max_ss = ss
    return max_ss


if __name__ == "__main__":
    day = "d8"
    with open(f"../inputs/{day}/input_simple.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
    with open(f"../inputs/{day}/input.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
