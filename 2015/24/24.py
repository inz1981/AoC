from itertools import combinations
from functools import reduce
from operator import mul


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        content = [int(c) for c in content.split("\n")]
    return content


def get_min_quantum_entanglement_group(weights: list, num_groups: int):
    group_size = sum(weights) // num_groups
    for i in range(len(weights)):

        group_qe = []
        for combo in combinations(weights, i):
            if sum(combo) == group_size:
                group_qe.append(reduce(mul, combo))
        if group_qe:
            return min(group_qe)


def part_1(path):
    weights = read_input_file(path)
    return get_min_quantum_entanglement_group(weights, 3)


def part_2(path):
    weights = read_input_file(path)
    return get_min_quantum_entanglement_group(weights, 4)


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "24_input.txt"
    ans = part_1(filepath)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "24_input.txt"
    ans = part_2(filepath)
    print(f"answer: {ans}")
