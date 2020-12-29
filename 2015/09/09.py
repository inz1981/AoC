import re
from itertools import permutations


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return [c for c in content.split("\n")]


def parse_data(data):
    route = []
    locations = []
    for d in data:
        src, target, dist = re.findall(r"(.*) to (.*) = (\d+)", d).pop()
        route.append((src, target, int(dist)))
        locations.append(src)
        locations.append(target)
    return route, list(set(locations))


def find_distance(routes: list, loc1: str, loc2: str):
    for r1, r2, dist in routes:
        if (loc1 in r1 or loc1 in r2) and (loc2 in r1 or loc2 in r2):
            return dist


def part_1(data):
    route_data, locations = parse_data(data)
    all_routes = permutations(locations)
    shortest = None
    for routes in all_routes:
        total_distance = 0
        for idx, r in enumerate(routes):
            if idx == 0:
                continue
            loc1 = routes[idx-1]
            loc2 = routes[idx]
            total_distance += find_distance(route_data, loc1, loc2)
        if not shortest:
            print(f"First ({routes}): {total_distance}")
            shortest = total_distance
        elif total_distance < shortest:
            print(f"new shortest! ({routes}): {total_distance}")
            shortest = total_distance
    return shortest


def part_2(data):
    route_data, locations = parse_data(data)
    all_routes = permutations(locations)
    longest = None
    for routes in all_routes:
        total_distance = 0
        for idx, r in enumerate(routes):
            if idx == 0:
                continue
            loc1 = routes[idx - 1]
            loc2 = routes[idx]
            total_distance += find_distance(route_data, loc1, loc2)
        if not longest:
            print(f"First ({routes}): {total_distance}")
            longest = total_distance
        elif total_distance > longest:
            print(f"new longest! ({routes}): {total_distance}")
            longest = total_distance
    return longest


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "09_input.txt"
    data = read_input_file(filepath)
    ans = part_1(data)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "09_input.txt"
    data = read_input_file(filepath)
    ans = part_2(data)
    print(f"answer: {ans}")
