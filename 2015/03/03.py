from typing import Dict


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return content


def part_1(data):

    grid = {
        (0, 0): 1
    }
    cur_loc = (0, 0)
    for dir in data:

        if dir == "^":
            cur_loc = (cur_loc[0], cur_loc[1]+1)
        elif dir == ">":
            cur_loc = (cur_loc[0]+1, cur_loc[1])
        elif dir == "v":
            cur_loc = (cur_loc[0], cur_loc[1]-1)
        elif dir == "<":
            cur_loc = (cur_loc[0]-1, cur_loc[1])

        if cur_loc in grid:
            grid[cur_loc] += 1
        else:
            grid[cur_loc] = 1
    ans = count_at_least_one(grid)
    return ans


def part_2(data):

    grid = {
        (0, 0): 2
    }
    santa_loc = (0, 0)
    robo_loc = (0, 0)
    for idx, dir in enumerate(data):

        if idx % 2:
            cur_loc = robo_loc
        else:
            cur_loc = santa_loc

        if dir == "^":
            cur_loc = (cur_loc[0], cur_loc[1]+1)
        elif dir == ">":
            cur_loc = (cur_loc[0]+1, cur_loc[1])
        elif dir == "v":
            cur_loc = (cur_loc[0], cur_loc[1]-1)
        elif dir == "<":
            cur_loc = (cur_loc[0]-1, cur_loc[1])

        if cur_loc in grid:
            grid[cur_loc] += 1
        else:
            grid[cur_loc] = 1

        if idx % 2:
            robo_loc = cur_loc
        else:
            santa_loc = cur_loc

    ans = count_at_least_one(grid)
    return ans


def count_at_least_one(grid: Dict):

    result = 0
    for _, presents in grid.items():
        if presents >= 1:
            result += 1
    return result


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "03_input.txt"
    data = read_input_file(filepath)
    ans = part_1(data)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "03_input.txt"
    data = read_input_file(filepath)
    ans = part_2(data)
    print(f"answer: {ans}")
