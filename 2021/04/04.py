def read_input_file(file_name: str):
    with open(file_name) as f:
        content = f.readline()
        numbers = content.replace("\n", "")
        numbers = [int(x) for x in numbers.split(",")]

        _ = f.readline()

        content = f.read()
        newlines = content.split("\n\n")
        boards = list()
        for line in newlines:
            board_lines = line.split("\n")
            board = list()
            for row in board_lines:
                row_n_checked = list()
                n_row = row.split()
                for x in n_row:
                    row_n_checked.append([int(x), False])
                board.append(row_n_checked)
            boards.append(board)

        return numbers, boards


def mark_num_on_board(num: int, board: list):
    for row in board:
        for col in row:
            if num == col[0]:
                col[1] = True


def check_if_won(board: list, dimension: int = 5):
    for x in range(dimension):
        # check columns
        if all(board[x][c][1] for c in range(dimension)):
            return True
        # check rows
        if all(board[r][x][1] for r in range(dimension)):
            return True
    return False


def get_unmarked_sum(board: list):
    result = 0
    for row in board:
        for col in row:
            if not col[1]:
                result += col[0]
    return result


def part_1():
    numbers, boards = read_input_file("input.txt")
    for num in numbers:
        for board in boards:
            mark_num_on_board(num, board)
            if check_if_won(board):
                return num * get_unmarked_sum(board)


def part_2():
    numbers, boards = read_input_file("input.txt")
    winning_boards_idx = []
    for num in numbers:
        for b_idx, board in enumerate(boards):
            if b_idx in winning_boards_idx:
                continue
            mark_num_on_board(num, board)
            if check_if_won(board):
                winning_boards_idx.append(b_idx)
                if len(boards) == len(winning_boards_idx):
                    return num * get_unmarked_sum(board)


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
