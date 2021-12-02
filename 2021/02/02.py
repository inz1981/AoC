def read_input_file(file_name: str):
    with open(file_name) as f:
        content = f.readlines()
        return [x.strip() for x in content]


def get_command_number(command_str):
    commands = ["forward ", "up ", "down "]
    for command in commands:
        if command in command_str:
            return command.strip(), int(command_str.replace(command, ""))


def part_1():
    course = read_input_file("input.txt")

    horizontal = 0
    depth = 0
    for direction in course:
        command, v = get_command_number(direction)
        if command == "forward":
            horizontal += v
        elif command == "up":
            depth -= v
        elif command == "down":
            depth += v
        else:
            raise ValueError(f"I don't understand you! {direction}")
    return horizontal * depth


def part_2():
    course = read_input_file("input.txt")

    horizontal = 0
    depth = 0
    aim = 0

    for direction in course:
        command, v = get_command_number(direction)
        if command == "forward":
            horizontal += v
            depth += (aim*v)
        elif command == "up":
            aim -= v
        elif command == "down":
            aim += v
        else:
            raise ValueError(f"I don't understand you! {direction}")
    return horizontal * depth


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
