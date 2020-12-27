import re


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return [c for c in content.split("\n")]


def create_grid():
    grid = {}
    for x in range(1000):
        for y in range(1000):
            grid[(x, y)] = "off"
    return grid


def create_grid_2():
    grid = {}
    for x in range(1000):
        for y in range(1000):
            grid[(x, y)] = 0
    return grid


def update_grid(start: tuple, end: tuple, action: str, grid: dict):
    for pos, val in grid.items():
        if (pos[0] >= start[0] and pos[1] >= start[1]) and (pos[0] <= end[0] and pos[1] <= end[1]):
            if action == "on":
                grid[pos] = "on"
            elif action == "off":
                grid[pos] = "off"
            else:
                if grid[pos] == "on":
                    grid[pos] = "off"
                else:
                    grid[pos] = "on"
    return grid


def update_grid_2(start: tuple, end: tuple, action: str, grid: dict):
    for pos, val in grid.items():
        if (pos[0] >= start[0] and pos[1] >= start[1]) and (pos[0] <= end[0] and pos[1] <= end[1]):
            if action == "on":
                grid[pos] += 1
            elif action == "off":
                if grid[pos] == 0:
                    continue
                else:
                    grid[pos] -= 1
            else:
                grid[pos] += 2
    return grid


def part_1(data):
    grid = create_grid()

    for idx, instruction in enumerate(data):
        start, end = re.findall(r"(\d+),(\d+)", instruction)
        start = tuple(int(x) for x in start)
        end = tuple(int(x) for x in end)

        if "on" in instruction:
            action = "on"
        elif "off" in instruction:
            action = "off"
        else:
            action = "toggle"
        grid = update_grid(start, end, action, grid)
        if not idx % 100:
            print(f"Done with instruction {idx}")
    return count_lit_lights(grid)


def count_lit_lights(data):
    result = 0
    for d, status in data.items():
        if status == "on":
            result += 1
    return result


def count_brightness(data):
    result = 0
    for d, status in data.items():
        result += status
    return result


def part_2(data):
    grid = create_grid_2()

    for idx, instruction in enumerate(data):
        start, end = re.findall(r"(\d+),(\d+)", instruction)
        start = tuple(int(x) for x in start)
        end = tuple(int(x) for x in end)

        if "on" in instruction:
            action = "on"
        elif "off" in instruction:
            action = "off"
        else:
            action = "toggle"
        grid = update_grid_2(start, end, action, grid)
        if not idx % 100:
            print(f"Done with instruction {idx}")
    return count_brightness(grid)


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "06_input.txt"
    data = read_input_file(filepath)

    ans = part_1(data)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "06_input.txt"
    data = read_input_file(filepath)
    ans = part_2(data)
    print(f"answer: {ans}")
