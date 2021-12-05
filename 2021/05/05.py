from collections import Counter
import math


def read_input_file(file_name: str):
    with open(file_name) as f:
        content = f.readlines()
        xy_range = [a.split(" -> ") for a in content]
        for xy_all in xy_range:
            for j, xy in enumerate(xy_all):
                xy_all[j] = xy.replace("\n", "")
        return xy_range


def get_plot_count(xy_data: list, diagonal=False):
    plot = []
    for xy_raw in xy_data:
        interval = []
        for xy in xy_raw:
            interval.append([int(a) for a in xy.split(",")])

        x1 = interval[0][0]
        x2 = interval[1][0]
        y1 = interval[0][1]
        y2 = interval[1][1]

        y_plots = list(range(min(y1, y2), max(y1, y2) + 1))
        x_plots = list(range(min(x1, x2), max(x1, x2) + 1))
        if x1 > x2:
            x_plots = [x for x in reversed(x_plots)]
        if y1 > y2:
            y_plots = [y for y in reversed(y_plots)]

        # diagonal
        if diagonal:
            if x1 != x2 and y1 != y2:
                for i, x in enumerate(x_plots):
                    plot.append((x, y_plots[i]))

        # horizontal/vertical
        if (x1 == x2) or (y1 == y2):
            if y1 != y2:
                plot.extend([(x1, y) for y in y_plots])
            if x1 != x2:
                plot.extend([(x, y1) for x in x_plots])

    two_or_more = [(count,) + p for p, count in Counter(plot).items() if count >= 2]
    return len(two_or_more)


def part_1():
    xy_data = read_input_file("input.txt")
    return get_plot_count(xy_data)


def part_2():
    xy_data = read_input_file("input.txt")
    return get_plot_count(xy_data, diagonal=True)


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
