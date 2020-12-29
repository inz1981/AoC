import re


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return [c for c in content.split("\n")]


def part_1(data):
    total = 0
    string_total = 0
    for string in data:
        total += len(string)
        string = string[1:-1]  # discard quotes
        string = string.replace("\\\\", "-")
        string = string.replace('\\\"', '-')
        string = re.sub('\\\\x[a-fA-F0-9]{2}', '-', string)
        string_total += len(string)
    return total-string_total


def part_2(data):
    string_total = 0
    total = 0
    for string in data:
        total += len(string)
        string = string.replace("\\", "\\\\")
        string = string.replace('"', '\\"')
        string = '"' + string + '"'
        string_total += len(string)
    return string_total-total


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "08_input.txt"
    data = read_input_file(filepath)
    ans = part_1(data)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "08_input.txt"
    data = read_input_file(filepath)
    ans = part_2(data)
    print(f"answer: {ans}")
