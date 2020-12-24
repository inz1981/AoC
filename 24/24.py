import copy
import re


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return [c for c in content.split("\n")]


def part_1(path):
    data = read_input_file(path)
    return flip_tiles(data)


def flip_tiles(data):
    grid_val = {
        "se": [0.5, -1],
        "sw": [-0.5, -1],
        "ne": [0.5, 1],
        "nw": [-0.5, 1],
        "w": [-1, 0.0],
        "e": [1, 0.0],
    }
    hex_grid = {
        (0.0, 0.0): "w"
    }
    for tile in data:
        tile_pos = re.findall(r"(se|sw|ne|nw|w|e)", tile)
        curr_pos = [0.0, 0.0]
        for pos in tile_pos:
            curr_pos = (curr_pos[0] + grid_val[pos][0], curr_pos[1] + grid_val[pos][1])
            if curr_pos not in hex_grid:
                hex_grid[(curr_pos[0], curr_pos[1])] = "w"
            # add neighbors if not existing.
            for neigh, neigh_pos_val in grid_val.items():
                neigh_pos = (neigh_pos_val[0] + curr_pos[0], neigh_pos_val[1] + curr_pos[1])
                if neigh_pos not in hex_grid:
                    hex_grid[neigh_pos] = "w"

        if hex_grid[curr_pos] == "b":
            tile_color = "w"
        else:
            tile_color = "b"
        hex_grid[(curr_pos[0], curr_pos[1])] = tile_color
    return grid_val, hex_grid


def day_flip(grid, grid_val, num_days):
    day_grid = copy.deepcopy(grid)
    total_black = 0
    for day in range(1, num_days+1):
        updated_grid = copy.deepcopy(day_grid)
        for pos, color in day_grid.items():
            num_black = 0
            # check neighbors
            for neigh, neigh_pos_val in grid_val.items():
                neigh_pos = (neigh_pos_val[0] + pos[0], neigh_pos_val[1] + pos[1])
                if neigh_pos in day_grid:
                    if day_grid[neigh_pos] == "b":
                        num_black += 1
                else:
                    updated_grid[neigh_pos] = "w"
            if (num_black == 0 or num_black > 2) and color == "b":
                updated_grid[pos] = "w"
            elif num_black == 2 and color == "w":
                updated_grid[pos] = "b"
        total_black = count_black(updated_grid)
        # print(f"Day {day}: {total_black}")
        day_grid = copy.deepcopy(updated_grid)
    return total_black


def count_black(hex_grid: dict) -> int:
    result = 0
    for pos, color in hex_grid.items():
        if color == "b":
            result += 1
    return result


def part_2(path):
    data = read_input_file(path)
    grid_val, grid = flip_tiles(data)
    return day_flip(grid, grid_val, 100)


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "24/24_input.txt"
    _, grid = part_1(filepath)
    ans = count_black(grid)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "24/24_input.txt"
    ans = part_2(filepath)
    print(f"answer: {ans}")
