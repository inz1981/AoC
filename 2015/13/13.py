from itertools import permutations
import re


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return [c for c in content.split("\n")]


def parse_data(data):
    result = {}
    for d in data:
        match = re.findall(r"(.*) would (gain \d+|lose \d+) .* next to (.*).", d)
        for person, points, neighbor in match:
            if "gain" in points:
                points = int(points.replace("gain ", ""))
            else:
                points = int(points.replace("lose ", "-"))
            if person not in result:
                result[person] = {neighbor: points}
            else:
                result[person][neighbor] = points
    return result


def part_1(data):
    seating_scores = parse_data(data)
    return find_optimal_seating_score(seating_scores)


def part_2(data):
    seating_scores = parse_data(data)

    seating_scores["Me"] = {}
    for person, v in seating_scores.items():
        if person == "Me":
            continue
        seating_scores[person]["Me"] = 0
        seating_scores["Me"][person] = 0

    return find_optimal_seating_score(seating_scores)


def find_optimal_seating_score(seating_scores):
    persons = list(seating_scores.keys())
    possible_seatings = list(permutations(persons))
    best_score = 0
    for seating in possible_seatings:
        seating_score = 0
        for idx, person in enumerate(seating):
            if idx == 0:
                n1pos = len(seating) - 1
            else:
                n1pos = idx - 1
            if idx == len(seating) - 1:
                n2pos = 0
            else:
                n2pos = idx + 1
            neighbor1 = seating[n1pos]
            neighbor2 = seating[n2pos]
            score = seating_scores[person][neighbor1] + seating_scores[person][
                neighbor2]
            seating_score += score

        if seating_score > best_score:
            print(f"{seating} has score: {seating_score}")
            best_score = seating_score
    return best_score


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "13_input.txt"
    data = read_input_file(filepath)
    ans = part_1(data)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "13_input.txt"
    data = read_input_file(filepath)
    ans = part_2(data)
    print(f"answer: {ans}")
