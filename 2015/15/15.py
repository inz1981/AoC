import re


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return [c for c in content.split("\n")]


def igscore(ig, ms, k):
    return max(sum([ing[k] * m for ing, m in zip(ig, ms)]), 0)


def score(ig, m):
    return igscore(
        ig, m, "capacity") * igscore(
        ig, m, "durability") * igscore(
        ig, m, "flavor") * igscore(
        ig, m, "texture"
    )


def find_max_score(ingredients, current, mass, remaining_weight, max_calories=0):
    if current == len(ingredients)-1:
        mass[current] = remaining_weight
        if max_calories and igscore(ingredients, mass, "calories") != max_calories:
            return 0
        return score(ingredients, mass)

    best_score = 0
    for m in range(1, remaining_weight):
        mass[current] = m
        best_score = max(best_score, find_max_score(
            ingredients, current+1, mass, remaining_weight-m, max_calories
        ))

    return best_score


def parse_data(data):
    ingredients = []
    for d in data:
        ingredient, properties = re.findall(r"(.*): (.*)", d).pop()
        properties = properties.split(",")
        ingred = {"name": ingredient}

        for prop in properties:
            prop_name, prop_value = re.findall(r"(.*) (-?\d+)", prop).pop()
            prop_name = prop_name.strip()
            prop_value = int(prop_value)
            ingred[prop_name] = prop_value
        ingredients.append(ingred)
    return ingredients


def part_1(data):
    ingredients = parse_data(data)
    return find_max_score(ingredients, 0, [0] * len(ingredients), 100)


def part_2(data):
    ingredients = parse_data(data)
    return find_max_score(ingredients, 0, [0] * len(ingredients), 100, max_calories=500)

if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "15_input.txt"
    data = read_input_file(filepath)
    ans = part_1(data)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "15_input.txt"
    data = read_input_file(filepath)
    ans = part_2(data)
    print(f"answer: {ans}")
