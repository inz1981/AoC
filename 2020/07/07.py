import re


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return content.split("\n")


def get_bag_deps(bags: str, req_map: dict):
    matches = re.findall(r"^(.*) bags contain (:?(\d+) (.*) bag|no other bags)", bags).pop()
    req_map[matches[0]] = dict()

    if any(t for t in matches if "no other bags" in t):
        return matches[0], req_map

    req_map[matches[0]][matches[3]] = {"amount": int(matches[2])}
    return matches[0], req_map


def parse_data(data: list, req_map: dict):
    for d in data:
        deps = d.split(",")
        bag_name, req_map = get_bag_deps(deps[0], req_map)
        i = 1
        while i < len(deps):
            amount, bag_child = re.findall(r"(\d+) (.*) bag", deps[i]).pop()
            req_map[bag_name][bag_child] = {"amount": int(amount)}
            i += 1


def find_parent_keys(d, target_key, parent_key=None):
    for k, v in d.items():
        if k == target_key:
            if parent_key:
                yield parent_key
        if isinstance(v, dict):
            for res in find_parent_keys(v, target_key, k):
                if res:
                    yield res


def get_bags_amount(d: dict, req_map):
    result = 1
    for k, v in d.items():
        result += get_bags_amount(req_map[k], req_map)*v["amount"]
    return result


def find_total(self, dct):
    total = 0
    for key, value in dct.iteritems():
        if isinstance(value, int):
            total += value
        if isinstance(value, dict):
            total += find_total(value)
    return total


if __name__ == '__main__':
    data = read_input_file("07_input.txt")
    req_map = dict()
    parse_data(data, req_map)

    parent_bags = tuple(find_parent_keys(req_map, "shiny gold"))
    ans = [parent for parent in parent_bags]
    for parent in parent_bags:
        ans.extend(tuple(find_parent_keys(req_map, parent)))

    sort_ans = sorted([x for x in ans])
    ans = set(sort_ans)
    print(sorted(ans))

    print("----- part 1 -----")
    print(f"answer: {len(ans)}")

    print("----- part 2 -----")

    tt = get_bags_amount(req_map["shiny gold"], req_map)
    print(f"answer: {tt-1}")

