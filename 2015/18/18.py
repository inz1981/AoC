import copy


def read_input_file(path):
    with open(path) as f:
        result = {}
        content = f.read()
    x_y = [c for c in content.split("\n")]
    len_x = len(x_y[0])
    len_y = len(x_y)
    for y in range(len_y):
        for x in range(len_x):
            result[(x, y)] = x_y[y][x]
    return result


def print_grid(grid: dict, dim=100):
    for y in range(dim):
        x_str = ""
        for x in range(dim):
            x_str += grid[(x, y)]
        print(x_str)


def neighbors(grid: dict, x: int, y: int):
    n = (x, y-1)
    nw = (x-1, y-1)
    ne = (x+1, y-1)
    w = (x-1, y)
    e = (x+1, y)
    sw = (x-1, y+1)
    s = (x, y+1)
    se = (x+1, y+1)

    result = ""
    if n in grid:
        result += grid[n]
    if nw in grid:
        result += grid[nw]
    if ne in grid:
        result += grid[ne]
    if w in grid:
        result += grid[w]
    if e in grid:
        result += grid[e]
    if sw in grid:
        result += grid[sw]
    if s in grid:
        result += grid[s]
    if se in grid:
        result += grid[se]
    on = result.count("#")
    off = result.count(".")
    return off, on


def animate_grid(grid: dict, dim, steps: int, corners=[]):

    for step in range(1, steps+1):

        new_grid = copy.deepcopy(grid)

        for y in range(dim):
            for x in range(dim):
                curr_state = grid[(x, y)]
                off, on = neighbors(grid, x, y)
                if curr_state == "#":
                    if on == 2 or on == 3:
                        continue
                    else:
                        if (x, y) not in corners:
                            new_grid[(x, y)] = "."
                else:
                    if on == 3:
                        new_grid[(x, y)] = "#"
        # print(f"After {step} step:")
        grid = copy.deepcopy(new_grid)

    return grid


def lights_on(grid, dim):
    on = 0
    for y in range(dim):
        for x in range(dim):
            if grid[(x, y)] == "#":
                on += 1
    return on


def part_1(data):
    steps = 100
    dimension = 100

    grid = animate_grid(data, dimension, steps)
    # print_grid(grid, dimension)

    on = lights_on(grid, dimension)
    return data, on


def part_2(data):
    steps = 100
    dimension = 100
    # init state:
    corners = [(0, 0), (0, dimension-1), (dimension-1, 0), (dimension-1, dimension-1)]
    for corner in corners:
        data[corner] = "#"
    # print_grid(data, dimension)

    grid = animate_grid(data, dimension, steps, corners)
    # print(f"After {steps} step:")
    # print_grid(grid, dimension)
    on = lights_on(grid, dimension)
    return data, on


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "18_input.txt"
    data = read_input_file(filepath)
    _, ans = part_1(data)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "18_input.txt"
    data = read_input_file(filepath)
    data, ans = part_2(data)
    print(f"answer: {ans}")
