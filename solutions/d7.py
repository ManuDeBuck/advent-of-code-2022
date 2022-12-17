import re


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"File({self.name}, {self.size})"


class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent_folder = parent
        self.sub_folders = []
        self.files = []

    def __repr__(self):
        return f"Folder({self.name}, {self.sub_folders}, {self.files})"

    def get_total_size(self):
        return sum([file.size for file in self.files]) \
               + sum([folder.get_total_size() for folder in self.sub_folders])

    def get_folder(self, name):
        for folder in self.sub_folders:
            if folder.name == name:
                return folder

    def add_folder(self, folder):
        self.sub_folders.append(folder)

    def add_file(self, file):
        self.files.append(file)

    def get_parent(self):
        return self.parent_folder

    def get_sub_folders(self):
        return self.sub_folders


def parse_tree(root_dir, cur_path, cur_dir, lines):
    if not len(lines):
        return
    command = lines.pop(0)
    if command == "$ ls":
        line = lines[0]
        while line and not line.startswith("$"):
            lines.pop(0)
            if line.startswith("dir"):
                folder_name = line.replace("dir ", "")
                cur_dir.add_folder(Folder(folder_name, cur_dir))
            else:
                file_size, file_name = re.match(r"^(.+) (.+)$", line).groups()
                cur_dir.add_file(File(file_name, int(file_size)))
            if len(lines):
                line = lines[0]
            else:
                line = None
        parse_tree(root_dir, cur_path, cur_dir, lines)
    elif command.startswith("$ cd"):
        folder_name = command.replace("$ cd ", "")
        if folder_name == "..":
            cur_path = re.sub(r"/[^/]+$", "", cur_path)
            cur_dir = cur_dir.get_parent()
            parse_tree(root_dir, cur_path, cur_dir, lines)
        elif folder_name == "/":
            parse_tree(root_dir, "/", root_dir, lines)
        else:
            if cur_dir.get_folder(folder_name) is None:
                cur_dir.add_folder(Folder(folder_name, cur_dir))
            d = cur_dir.get_folder(folder_name)
            parse_tree(root_dir, cur_path + "/" + folder_name, d, lines)


def solve_1(input):
    def get_size_r(folder):
        sum = 0
        if folder.get_total_size() < 100000:
            sum += folder.get_total_size()
        for sub_folder in folder.get_sub_folders():
            sum += get_size_r(sub_folder)
        return sum

    input.pop(0)  # always start at root dir
    root_dir = Folder("", None)
    parse_tree(root_dir, "/", root_dir, input)
    return get_size_r(root_dir)


def solve_2(input):
    def get_smallest_r(folder, cur_min):
        if folder.get_total_size() > to_free:
            cur_min = min(cur_min, folder.get_total_size())
        for sub_folder in folder.get_sub_folders():
            cur_min = min(cur_min, get_smallest_r(sub_folder, cur_min))
        return cur_min

    input.pop(0)  # always start at root dir
    root_dir = Folder("", None)
    parse_tree(root_dir, "/", root_dir, input)

    total = 70000000
    needed = 30000000
    current = root_dir.get_total_size()
    to_free = needed - (total - current)
    return get_smallest_r(root_dir, root_dir.get_total_size())


if __name__ == "__main__":
    day = "d7"
    with open(f"../inputs/{day}/input_simple.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
    with open(f"../inputs/{day}/input.txt") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]
        print(f"solution to puzzle 1 {solve_1(lines[:])}")
        print(f"solution to puzzle 2 {solve_2(lines[:])}")
