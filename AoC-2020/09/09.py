import itertools


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return [int(c) for c in content.split("\n")]


def find_integers_sum(data: list, next_sum: int):
    result = []
    for numbers in itertools.combinations(data, 2):
        if sum(numbers) == next_sum:
            result.append([number for number in numbers])
    return result


def find_sum_of_err(data: list, target: int):
    for i in range(0, len(data)):
        for j in range(len(data) - i + 1):
            if len(data[j:j + i]) > 1 and sum(data[j:j + i]) == target:
                print(data[j:j + i])
                return min(data[j:j + i]) + max(data[j:j + i])


def iterate_xmas(data: list, preamble: int):
    for idx in range(0, len(data)):
        if (idx + preamble) > len(data)-1:
            break
        numbers = find_integers_sum(data[idx:preamble+idx], data[idx+preamble])
        if not numbers:
            return data[idx+preamble]


def part_1():
    data = read_input_file("09/09_input.txt")
    return iterate_xmas(data, 25)


def part_2():
    data = read_input_file("09/09_input.txt")
    err_sum = iterate_xmas(data, 25)
    min_max = find_sum_of_err(data, err_sum)
    return min_max


if __name__ == '__main__':
    print("----- part 1 -----")
    data = part_1()
    print(f"answer: {data}")

    print("----- part 2 -----")
    data = part_2()
    print(f"answer: {data}")
