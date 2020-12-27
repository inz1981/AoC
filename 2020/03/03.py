def read_input_file_test():
    with open('03_input_test.txt') as f:
        content = f.readlines()
        return [x.strip() for x in content]


def read_input_file(path):
    with open(path) as f:
        content = f.readlines()
        return [x.strip() for x in content]


def extend_x_coordinates(coords):
    for y, x in enumerate(coords):
        coords[y] = x + x
    return coords


def traverse_map(inc_x, inc_y, tree_map):
    curr_x = 0
    curr_y = 0
    trees = 0
    y_max = len(tree_map)
    while curr_y < y_max:
        x_map = tree_map[curr_y]
        if curr_x > len(x_map):
            extend_x_coordinates(tree_map)
        if tree_map[curr_y][curr_x] == "#":
            trees = trees + 1
        curr_x = curr_x + inc_x
        curr_y = curr_y + inc_y
        if curr_y > y_max:
            return trees, tree_map
    return trees, tree_map


def multiply_list(my_list):
    result = 1
    for x in my_list:
        result = result * x
    return result


if __name__ == '__main__':

    print("----- part 1 -----")
    tree_map = read_input_file("03_input.txt")
    trees, tree_map = traverse_map(3, 1, tree_map)
    print(f"num trees: {trees}")

    print("----- part 2 -----")
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = list()
    for slope in slopes:
        slope_trees, _ = traverse_map(slope[0], slope[1], tree_map)
        trees.append(slope_trees)
    print(trees)
    mult_trees = multiply_list(trees)
    print(f"trees multi: {mult_trees}")
