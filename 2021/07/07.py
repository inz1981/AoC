import math


def read_input_file(file_name: str):
    with open(file_name) as f:
        content = f.readline()
        d = content.split(",")
        return [int(x) for x in d]


def part_1():
    crabs = read_input_file("input.txt")
    crabs.sort()
    c = 0
    for x in crabs:
        c += abs(x-crabs[len(crabs)//2])
    return c


def part_2():
    crabs = read_input_file("input.txt")
    crabs.sort()

    avg_pos_down = math.ceil(sum(crabs) / len(crabs))
    avg_pos_up = math.floor(sum(crabs) / len(crabs))

    c_up = avg_total_fuel(avg_pos_up, crabs)
    c_down = avg_total_fuel(avg_pos_down, crabs)
    return c_up if c_up < c_down else c_down


def avg_total_fuel(avg_pos_up, crabs):
    c = 0
    for x in crabs:
        f = abs(avg_pos_up - x)
        for fstep in range(1, f + 1):
            c += fstep
    return c


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
