def read_input_file(path):
    with open(path) as f:
        content = f.read()
        lines = [int(c) for c in content.split(",")]
        return lines


def play(start_numbers, stop_turn):
    last_num = None
    said_numbers = {}
    for turn, num in enumerate(start_numbers):
        said_numbers[num] = [turn + 1]
        last_num = num
    starting_len = len(said_numbers)
    for turn in range(starting_len + 1, stop_turn + 1):
        if last_num in said_numbers and len(said_numbers[last_num]) == 1:
            if 0 in said_numbers:
                said_numbers[0].append(turn)
            else:
                said_numbers[0] = [turn]
            last_num = 0
        elif last_num in said_numbers and len(said_numbers[last_num]) > 1:
            diff = said_numbers[last_num][len(said_numbers[last_num]) - 1] - \
                   said_numbers[last_num][len(said_numbers[last_num]) - 2]
            last_num = diff
            if diff not in said_numbers:
                said_numbers[diff] = [turn]
            else:
                said_numbers[diff].append(turn)
    print(f"{stop_turn}th number said: {last_num}")
    return last_num


def part_1(path):
    starting_numbers = read_input_file(path)
    return play(starting_numbers, 2020)


def part_2(path):
    data = read_input_file(path)
    return play(data, 30000000)


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "15/15_input.txt"
    ans = part_1(filepath)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "15/15_input.txt"
    ans = part_2(filepath)

    print(f"answer: {ans}")
