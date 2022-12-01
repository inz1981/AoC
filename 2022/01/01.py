def read_input_file(file_name: str):
    with open(file_name) as f:
        content = f.read()
        elves_food = content.split("\n\n")
        result = []
        for cal in elves_food:
            cals = cal.split("\n")
            elf_calories = [int(c) for c in cals]
            result.append(elf_calories)
        return result


def part_1():
    elves_cals = read_input_file("input.txt")
    highest_cal = 0

    for elf in elves_cals:
        sum_cal = sum(elf)
        if sum_cal >= highest_cal:
            highest_cal = sum_cal

    return highest_cal


def part_2():
    elves_cals = read_input_file("input.txt")
    highest_cal = [0, 0, 0]

    for elf in elves_cals:
        sum_cal = sum(elf)
        minpos = highest_cal.index(min(highest_cal))
        if sum_cal > highest_cal[minpos]:
            highest_cal[minpos] = sum_cal

    return sum(highest_cal)


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
