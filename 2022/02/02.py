def read_input_file(file_name: str):
    with open(file_name) as f:
        """Each line as string."""
        content = f.readlines()
        return [x.strip().split(" ") for x in content]


def get_hand_score(command: str):
    if command == "A" or command == "X":
        return 1
    elif command == "B" or command == "Y":
        return 2
    elif command == "C" or command == "Z":
        return 3
    raise ValueError("Unknown command!")


def part_1():
    # A for Rock, B for Paper, and C for Scissors.
    # X for Rock, Y for Paper, and Z for Scissors.
    x_cond = ["A", "B", "C"]
    y_cond = ["X", "Y", "Z"]
    # Score: shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    # + (0 if you lost, 3 if the round was a draw, and 6 if you won).
    score = 0
    d = read_input_file("input.txt")

    for opp, you in d:
        x_idx = x_cond.index(opp)
        y_idx = y_cond.index(you)

        if x_idx == y_idx:
            score += 3+get_hand_score(you)
        elif x_idx == 0 and y_idx == 1:
            score += 6 + get_hand_score(you)
        elif x_idx == 0 and y_idx == 2:
            score += get_hand_score(you)
        elif x_idx == 1 and y_idx == 0:
            score += get_hand_score(you)
        elif x_idx == 1 and y_idx == 2:
            score += 6+get_hand_score(you)
        elif x_idx == 2 and y_idx == 0:
            score += 6+get_hand_score(you)
        elif x_idx == 2 and y_idx == 1:
            score += get_hand_score(you)
    return score


def part_2():
    # X means you need to lose
    # Y means you need to end the round in a draw
    # Z means you need to win.
    d = read_input_file("input.txt")
    # A for Rock, B for Paper, and C for Scissors.
    score = 0
    for opp, you in d:
        if you == "X":  # Lose
            if opp == "A":
                score += get_hand_score("Z")
            elif opp == "B":
                score += get_hand_score("X")
            elif opp == "C":
                score += get_hand_score("Y")
        elif you == "Y":  # Draw
            score += 3+get_hand_score(opp)
        elif you == "Z":  # Win
            if opp == "A":
                score += 6+get_hand_score("Y")
            elif opp == "B":
                score += 6+get_hand_score("Z")
            elif opp == "C":
                score += 6+get_hand_score("X")
    return score


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
