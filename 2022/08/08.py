def read_input_file(file_name: str):
    with open(file_name) as f:
        """Each line as integer."""
        trees = [x.strip() for x in f.readlines()]
        res = []
        for y in range(len(trees)):
            yl = []
            for x in range(len(trees[y])):
                yl.append(int(trees[y][x]))
            res.append(yl)
        return res


def is_vertical_visable(range: list, tree_map: list, current_tree_len: int, x: int):
    count_trees = 0
    for y in range:
        count_trees += 1
        if tree_map[y][x] >= current_tree_len:
            return False, count_trees
    return True, count_trees


def is_horizontal_visable(range: list, tree_map: list, current_tree_len: int, y: int):
    count_trees = 0
    for x in range:
        count_trees += 1
        if tree_map[y][x] >= current_tree_len:
            return False, count_trees
    return True, count_trees


def part_1():
    tree_map = read_input_file("input.txt")
    c = 0
    for y in range(1, len(tree_map)-1):
        for x in range(1, len(tree_map[y])-1):
            t_len = tree_map[y][x]
            if (is_vertical_visable(list(range(0, y)), tree_map, t_len, x)[0] or
                    is_horizontal_visable(list(range(0, x)), tree_map, t_len, y)[0] or
                    is_vertical_visable(list(range(y+1, len(tree_map))), tree_map, t_len, x)[0] or
                    is_horizontal_visable(list(range(x+1, len(tree_map[y]))), tree_map, t_len, y)[0]):
                c += 1
                continue

    return c + len(tree_map)*2 + (len(tree_map[0])*2-4)


def part_2():
    tree_map = read_input_file("input.txt")

    result = []
    for y in range(1, len(tree_map) - 1):
        for x in range(1, len(tree_map[y]) - 1):
            t_len = tree_map[y][x]
            up = is_vertical_visable(list(reversed(range(0, y))), tree_map, t_len, x)[1]
            left = is_horizontal_visable(list(reversed(range(0, x))), tree_map, t_len, y)[1]
            right = is_horizontal_visable(list(range(x+1, len(tree_map[y]))), tree_map, t_len, y)[1]
            down = is_vertical_visable(list(range(y+1, len(tree_map))), tree_map, t_len, x)[1]
            result.append(up*left*right*down)
    return max(result)


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
