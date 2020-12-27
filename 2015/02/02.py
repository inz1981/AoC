from typing import List


def read_input_file(path):
    with open(path) as f:
        result = []
        content = f.read()
        dimensions = [c for c in content.split("\n")]
        for dimension in dimensions:
            dim = dimension.split("x")
            dim = [int(d) for d in dim]
            result.append(dim)
        return result


def get_sq_feet_of_package_wrap(dimensions: List[List]):
    total_sq = 0
    for dim in dimensions:
        sq_feet = (2*dim[0]*dim[1]) + (2*dim[1]*dim[2]) + (2*dim[2]*dim[0])
        min_side = min(dim)
        dim.remove(min_side)
        min_side2 = min(dim)
        slack = min_side * min_side2
        total_sq += sq_feet + slack
    return total_sq


def get_sq_feet_of_package_ribbon(dimensions: List[List]):
    total_sq = 0
    for dim in dimensions:
        ribbon_bow_sq = dim[0] * dim[1] * dim[2]
        min_side = min(dim)
        dim.remove(min_side)
        min_side2 = min(dim)
        ribbon_sq = min_side + min_side + min_side2 + min_side2
        total_sq += ribbon_bow_sq + ribbon_sq
    return total_sq


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "02_input.txt"
    data = read_input_file(filepath)
    ans = get_sq_feet_of_package_wrap(data)
    print(f"answer: {ans} sq feet.")

    print("----- part 2 -----")
    filepath = "02_input.txt"
    data = read_input_file(filepath)
    ans = get_sq_feet_of_package_ribbon(data)
    print(f"answer: {ans}")
