def read_input_file(path):
    with open(path) as f:
        content = f.read()
        lines = [str(c) for c in content.split("\n")]
        return lines


def get_action_values(s: str):
    return s[0], int(s[1:])


def calc_manhattan_distance(data: dict):
    ns = max(data["N"], data["S"]) - min(data["N"], data["S"])
    ew = max(data["E"], data["W"]) - min(data["E"], data["W"])
    return int(ns+ew)


def part_1(path):
    data = read_input_file(path)

    pos = "E"
    course = {
        "N": 0,
        "S": 0,
        "E": 0,
        "W": 0,
    }
    for d in data:
        action, value = get_action_values(d)
        if action == "F":
            course[pos] += value
        if action in course.keys():
            course[action] += value
        if action in ["L", "R"]:
            pos = turn(pos, value, action)
    return course


def part_2(path):
    data = read_input_file(path)

    pos = "E"
    course = {
        "N": 0,
        "E": 0,
        "S": 0,
        "W": 0,
    }
    waypoint = {
        "N": 1,
        "E": 10,
        "S": 0,
        "W": 0,
    }
    for d in data:
        action, value = get_action_values(d)
        if action == "F":
            for w, v in waypoint.items():
                curr_w = v*value
                course[w] += curr_w
        if action in course.keys():
            waypoint[action] = waypoint[action]+value
        if action in ["L", "R"]:
            waypoint = turn(pos, value, action, waypoint)
    print(f"way: {waypoint}")
    return course


def turn(pos, value, direction, waypoint=None):
    comp = ["N", "E", "S", "W"]
    points = int(value / 90)
    if direction == "L":
        points = -points

    if not waypoint:
        if pos == "N":
            newpos = comp[points % len(comp)]
        elif pos == "E":
            newpos = comp[(points + 1) % len(comp)]
        elif pos == "S":
            newpos = comp[(points + 2) % len(comp)]
        elif pos == "W":
            newpos = comp[(points + 3) % len(comp)]
        print(f"direction ({direction}) changed to {newpos}")
        return newpos
    else:
        old_waypoint = waypoint.copy()
        for way in waypoint:
            if way == "N":
                newpos = comp[points % len(comp)]
                waypoint[newpos] = old_waypoint[way]
            elif way == "E":
                newpos = comp[(points + 1) % len(comp)]
                waypoint[newpos] = old_waypoint[way]
            elif way == "S":
                newpos = comp[(points + 2) % len(comp)]
                waypoint[newpos] = old_waypoint[way]
            elif way == "W":
                newpos = comp[(points + 3) % len(comp)]
                waypoint[newpos] = old_waypoint[way]
        return waypoint


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "12_input.txt"
    data = part_1(filepath)
    ans = calc_manhattan_distance(data)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "12_input.txt"
    data = part_2(filepath)
    ans = calc_manhattan_distance(data)
    print(f"answer: {ans}")
