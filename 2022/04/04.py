def read_input_file(file_name: str):
    with open(file_name) as f:
        """Each line as string."""
        content = f.readlines()
        return [x.strip() for x in content]


def part_1():
    dd = read_input_file("input.txt")
    count = 0
    for x in dd:
        e1, e2 = x.split(",")
        e1_min, e1_max = e1.split("-")
        e2_min, e2_max = e2.split("-")

        e1l = list(range(int(e1_min), int(e1_max) + 1))
        e2l = list(range(int(e2_min), int(e2_max) + 1))
        if all(c in e2l for c in e1l) or all(c in e1l for c in e2l):
            count += 1
    return count


def part_2():
    dd = read_input_file("input.txt")
    count = 0
    for x in dd:
        e1, e2 = x.split(",")
        e1_min, e1_max = e1.split("-")
        e2_min, e2_max = e2.split("-")

        e1l = list(range(int(e1_min), int(e1_max) + 1))
        e2l = list(range(int(e2_min), int(e2_max) + 1))
        if any(c in e2l for c in e1l) or any(c in e1l for c in e2l):
            count += 1
    return count


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
