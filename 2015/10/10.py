def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return [c for c in content.split("\n")]


def play_times(data: str, num_times: int):
    time_data = ""

    for time in range(num_times):
        num_consecutive = 1
        for idx, curr_digit in enumerate(data):
            if idx == 0:
                continue
            prev_digit = data[idx-1]
            if prev_digit == curr_digit:
                num_consecutive += 1
                if idx == len(data)-1:
                    time_data += str(num_consecutive)+curr_digit
                    data = time_data
            else:
                time_data += str(num_consecutive) + prev_digit
                num_consecutive = 1
                if idx == len(data) - 1:
                    time_data += "1"+curr_digit
                    data = time_data
        time_data = ""
    return len(data)


def part_1(data):
    return play_times(data, 40)


def part_2(data):
    return play_times(data, 50)


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "10_input.txt"
    data = read_input_file(filepath)
    ans = part_1(data.pop())
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "10_input.txt"
    data = read_input_file(filepath)
    ans = part_2(data.pop())
    print(f"answer: {ans}")
