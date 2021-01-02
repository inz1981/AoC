import json
import re


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return [c for c in content.split("\n")]


def read_json_file(path):
    with open(path) as f:
        return json.load(f)


def part_1(filepath):
    with open(filepath) as f:
        content = f.read()
    numbers = re.findall(r"([0-9]+|-[0-9]+)", content)
    return sum([int(x) for x in numbers])


def part_2(data):
    return iterate_json(data)


def iterate_json(data):
    if type(data) == int:
        return data
    if type(data) == list:
        return sum([iterate_json(data) for data in data])
    if type(data) != dict:
        return 0
    if 'red' in data.values():
        return 0
    return iterate_json(list(data.values()))


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "12_input.json"
    ans = part_1(filepath)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "12_input.json"
    data = read_json_file(filepath)
    ans = part_2(data)
    print(f"answer: {ans}")
