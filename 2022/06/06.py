def read_input_file(file_name: str):
    with open(file_name) as f:
        content = f.readline()
        return content


def is_unique(st):
    char_set = []
    for i in range(0, len(st)):
        if st[i] in char_set:
            return False
        char_set.append(st[i])
    return True


def part_1():
    chars = read_input_file("input.txt")

    for x in range(0, len(chars)):
        if is_unique(chars[x:x + 4]):
            return x+4


def part_2():
    chars = read_input_file("input.txt")

    for x in range(0, len(chars)):
        if is_unique(chars[x:x + 14]):
            return x + 14


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
