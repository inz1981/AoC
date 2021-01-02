import re


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return [c for c in content.split("\n")]


def parse_data(data: list):
    reindeer_data = {}
    for d in data:
        name, speed, fly_time, rest_time = re.findall(
            r"(.*) can fly (\d+) km/s for (\d+) .* for (\d+) seconds.", d
        ).pop()
        reindeer_data[name] = {
            "fly_time": int(fly_time),
            "speed": int(speed),
            "rest_time": int(rest_time),
            "fly_rest_time": int(fly_time) + int(rest_time),
            "distance": 0,
            "is_flying": True,
            "fly_time_left": int(fly_time),
            "rest_time_left": int(rest_time),
            "points": 0,
        }
    return reindeer_data


def get_flight_distance(reindeer_data: dict, total_time: int):
    longest_distance = 0
    for name, values in reindeer_data.items():
        fly_rest_total = int(total_time / values["fly_rest_time"])
        rest = total_time % values["fly_rest_time"]
        if rest >= values["fly_time"]:
            fly_rest_total += 1
            distance = fly_rest_total * values["speed"] * values["fly_time"]
        else:
            distance = fly_rest_total * values["speed"] * values["fly_time"]
            distance += rest * values["speed"]
        print(f"{name} flew {distance} km!")
        if distance > longest_distance:
            print(f"{name} new leader!")
            longest_distance = distance
    return longest_distance


def get_flight_points(reindeer_data: dict, total_time: int):

    winning_points = 0

    for sec in range(1, total_time+1):

        for name, values in reindeer_data.items():
            if values["is_flying"]:
                values["distance"] += values["speed"]
                values["fly_time_left"] -= 1
                if not values["fly_time_left"]:
                    values["is_flying"] = False
                    values["fly_time_left"] = values["fly_time"]
            else:
                values["rest_time_left"] -= 1
                if not values["rest_time_left"]:
                    values["is_flying"] = True
                    values["rest_time_left"] = values["rest_time"]

        # check leader
        distances = [[values["distance"], name] for name, values in reindeer_data.items()]
        leaders = []
        longest_distance = 0
        for distance, name in distances:
            if not longest_distance:
                longest_distance = distance
                leaders.append(name)
                continue
            if distance > longest_distance:
                longest_distance = distance
                leaders = [name]
            elif distance == longest_distance:
                leaders.append(name)
                longest_distance = distance
        for leader in leaders:
            reindeer_data[leader]["points"] += 1
    return reindeer_data


def get_winning_reinder_point(reindeer_data: dict):
    most_points = 0
    winning_reindeer = {}
    for name, values in reindeer_data.items():
        if values["points"] > most_points:
            most_points = values["points"]
            winning_reindeer = {name: reindeer_data[name]}
    return winning_reindeer, most_points


def part_1(data):
    reindeer_data = parse_data(data)
    return get_flight_distance(reindeer_data, 2503)


def part_2(data):
    reindeer_data = parse_data(data)
    return get_flight_points(reindeer_data, 2503)


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "14_input.txt"
    data = read_input_file(filepath)
    ans = part_1(data)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "14_input.txt"
    data = read_input_file(filepath)
    data = part_2(data)
    data, ans = get_winning_reinder_point(data)
    print(f"answer: {ans}")
