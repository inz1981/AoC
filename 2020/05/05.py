import re
from operator import itemgetter


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return content.split("\n")


def find_row_col_and_id(seat: str):
    row_top = 127
    row_bottom = 0
    col_top = 7
    col_bottom = 0
    rows, cols = re.findall(r"([F|B]{7})([L|R]{3})", seat).pop()
    for row in rows:
        if row == "F":
            row_top = int(row_top - (row_top - row_bottom) / 2)
        elif row == "B":
            row_bottom = int(row_bottom + (row_top - row_bottom) / 2) + 1

    for col in cols:
        if col == "L":
            col_top = int(col_top - (col_top - col_bottom) / 2)
        elif col == "R":
            col_bottom = int(col_bottom + (col_top - col_bottom) / 2) + 1

    seat_id = (row_top*8) + col_top

    return row_top, col_top, seat_id


def part_1():
    seats = read_input_file("05_input.txt")
    boarding_passes = list()
    for seat in seats:
        row, col, seat_id = find_row_col_and_id(seat)
        # print(f"{seat} is: row:{row}, col:{col}, seat_id: {seat_id}")
        boarding_passes.append((seat, row, col, seat_id))

    return max(boarding_passes, key=itemgetter(1))[3], boarding_passes


def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst]


def part_2():
    _, boarding_passes = part_1()
    boarding_passes.sort(key=lambda x: x[3])
    seat_ids = [x[3] for x in boarding_passes]
    return find_missing(seat_ids)


if __name__ == '__main__':
    print("----- part 1 -----")
    highest_id, _ = part_1()
    print(f"Highest seat id: {highest_id}")

    print("----- part 2 -----")
    data = part_2()
    print(f"My seat id:: {data}")
