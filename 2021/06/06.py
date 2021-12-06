def read_input_file(file_name: str):
    with open(file_name) as f:
        content = f.readline()
        fish = content.split(",")
        return [int(x) for x in fish]


def part_1():
    fish = read_input_file("input.txt")

    print(f"Initial state: {fish}")
    day = 1
    end_day = 80

    while day < end_day + 1:
        for i in range(len(fish)):
            fish[i] -= 1
            if fish[i] == -1:
                fish[i] = 6
                fish.append(8)
        print(f"After  {day} day:  {fish}")
        day += 1
    return len(fish)


def part_2():
    fish = read_input_file("input.txt")

    return len(fish)


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
