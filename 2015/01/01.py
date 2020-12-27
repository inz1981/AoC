def read_input_file(path):
    with open(path) as f:
        return f.read()


def move_to_basement(data):
    curr_floor = 0
    for idx, dir in enumerate(data):
        if dir == "(":
            curr_floor += 1
        else:
            curr_floor -= 1
        if curr_floor == -1:
            return idx + 1


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "01_input.txt"
    data = read_input_file(filepath)
    ans = data.count("(") - data.count(")")
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "01_input.txt"
    data = read_input_file(filepath)
    ans = move_to_basement(data)
    print(f"answer: {ans}")
