import re


def read_input_file(file_name: str):
    with open(file_name) as f:
        """Each line as string."""
        content = f.readlines()
        return [x.strip() for x in content]


def part_1():
    d = read_input_file("input.txt")

    fs = create_file_tree(d)

    ans = 0
    for k, v in fs.items():
        if v <= 100000:
            ans += v

    return ans


def part_2():
    d = read_input_file("input.txt")

    fs = create_file_tree(d)

    total_space = 70000000
    total_free = total_space - fs["/"]
    total_free_up = 30000000 - total_free

    options = []
    for _, v in fs.items():
        if v >= total_free_up:
            options.append(v)

    return min(options)


def create_file_tree(commands: list):
    fs = {
        "/": 0
    }

    tree = []
    for cmd in commands:
        if cmd.startswith("$"):
            if "cd" in cmd:
                directory = cmd[5:]
                if directory == "..":
                    tree.pop()
                else:
                    tree.append(directory)
            if "ls" in cmd:
                pass
        else:
            size_file = re.findall(r"(\d+) (.*)", cmd)
            if size_file:
                size = int(size_file[0][0])
                path = ""
                for p in tree:
                    if p == "/":
                        path = "/"
                    else:
                        path += f"{p}/"
                    if path in fs:
                        fs[path] += size
                    else:
                        fs[path] = size
    return fs


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
