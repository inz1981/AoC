import string


def read_input_file(file_name: str):
    with open(file_name) as f:
        """Each line as string."""
        content = f.readlines()
        return [x.strip() for x in content]


def part_1():
    d = read_input_file("input.txt")
    prio = 0
    for pack in d:
        comp1, comp2 = pack[:len(pack)//2], pack[len(pack)//2:]
        for item in comp1:
            if item in comp2:
                prio += string.ascii_letters.find(item) + 1
                break
    return prio


def part_2():
    d = read_input_file("input.txt")
    prio = 0
    i = 0
    while i < len(d):
        for item in d[i]:
            if item in d[i+1] and item in d[i+2]:
                prio += string.ascii_letters.find(item) + 1
                break
        i += 3
    return prio


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
