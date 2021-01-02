import re


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return [c for c in content.split("\n")]


def parse_data(data):
    sues = []
    for d in data:
        suenr, properties = re.findall(r"(Sue \d+): (.*)", d).pop()
        properties = properties.split(",")
        sue = {}

        for prop in properties:
            prop_name, prop_value = re.findall(r"(.*): (\d+)", prop).pop()
            prop_name = prop_name.strip()
            prop_value = int(prop_value)
            sue[prop_name] = prop_value
        sues.append(sue)
    return sues


def validate_sue(sue: dict, mfcsam: dict):
    for k, v in sue.items():
        if k in mfcsam and mfcsam[k] == v:
            continue
        else:
            return False
    return True


def validate_real_sue(sue: dict, mfcsam: dict):
    for k, v in sue.items():
        if k in mfcsam:
            if k in ["cats", "trees"]:
                if v > mfcsam[k]:
                    continue
                else:
                    return False
            if k in ["pomeranians", "goldfish"]:
                if v < mfcsam[k]:
                    continue
                else:
                    return False
            if v == mfcsam[k]:
                continue
            else:
                return False
        else:
            return False
    return True


def part_1(data):
    sues = parse_data(data)
    MFCSAM_DATA = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    for sue_nr, sue in enumerate(sues):
        if validate_sue(sue, MFCSAM_DATA, sue_nr+1):
            print(f"Gotcha Sue{sue_nr+1}!")
            return sue_nr+1
    return 0


def part_2(data):
    sues = parse_data(data)
    MFCSAM_DATA = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    for sue_nr, sue in enumerate(sues):
        if validate_real_sue(sue, MFCSAM_DATA, sue_nr + 1):
            print(f"Gotcha Sue{sue_nr + 1}!")
            return sue_nr + 1
    return 0


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "16_input.txt"
    data = read_input_file(filepath)
    ans = part_1(data)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "16_input.txt"
    data = read_input_file(filepath)
    ans = part_2(data)
    print(f"answer: {ans}")
