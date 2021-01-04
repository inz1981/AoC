import numpy as np


def read_input_file(path):
    with open(path) as f:
        content = f.read()
    return int(content)


def part_1(path):
    min_presents = read_input_file(path)
    houses = np.zeros(int(min_presents/10))
    for elf in range(1, int(min_presents/10)):
        houses[elf::elf] += 10 * elf
    return np.nonzero(houses >= min_presents)[0][0]


def part_2(path):
    min_presents = read_input_file(path)
    houses = np.zeros(int(min_presents/10))
    for elf in range(1, int(min_presents/10)):
        houses[elf:(elf + 1) * 50:elf] += 11 * elf
    return np.nonzero(houses >= min_presents)[0][0]


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "20_input.txt"
    ans = part_1(filepath)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "20_input.txt"
    ans = part_2(filepath)
    print(f"answer: {ans}")
