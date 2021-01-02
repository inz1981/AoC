from itertools import combinations, permutations


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return sorted([int(c) for c in content.split("\n")])


def part_1(data):

    wanted = 150
    result = []
    for num in range(2, len(data)+1):
        combos = list(combinations(data, num))
        for combo in combos:
            if sum(combo) == wanted:
                result.append(combo)

    print(result)

    return result


def part_2(data):
    data = part_1(data)

    min_cont = len(data)
    for d in data:
        if len(d) < min_cont:
            print(f"Yes: {d}")
            min_cont = len(d)

    result = []
    for d in data:
        if len(d) == min_cont:
            result.append(d)

    return len(result)


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "17_input.txt"
    data = read_input_file(filepath)
    ans = part_1(data)
    print(f"answer: {len(ans)}")

    print("----- part 2 -----")
    filepath = "17_input.txt"
    data = read_input_file(filepath)
    ans = part_2(data)
    print(f"answer: {ans}")
