def read_input_file(file_name: str):
    with open(file_name) as f:
        content = f.readlines()
        res = []
        for c in content:
            sigs, digs = c.split(" | ")
            res.append(digs.replace("\n", ""))
        return res


def part_1():
    digs = read_input_file("input.txt")

    d = []
    for dig in digs:
        dig_list = dig.split()
        for x in dig_list:
            d.append(x)

    w_nums = [2, 3, 4, 7]
    res = 0
    for x in d:
        if len(x) in w_nums:
            res += 1
    return res


def part_2():
    return read_input_file("input_test.txt")


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
