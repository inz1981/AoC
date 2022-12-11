import re
from math import prod


def read_input_file(file_name: str) -> dict:
    with open(file_name) as f:
        content = f.read()
        newlines = content.split("\n\n")
        monkey_input = [line for line in newlines]

        monkeys = {}
        for nr, input in enumerate(monkey_input):
            m_data = input.split("\n")
            items = re.findall("(\d+)+", m_data[1])
            items = [int(item) for item in items]
            monkey = {
                nr: {
                    "items": items,
                    "operation": m_data[2][m_data[2].rfind("=")+2:],
                    "test": {
                        "division": int(re.findall("(\d+)", m_data[3])[0]),
                        "true": int(re.findall("(\d+)", m_data[4])[0]),
                        "false": int(re.findall("(\d+)", m_data[5])[0]),
                    },
                    "inspections": 0
                }
            }
            monkeys.update(monkey)
        return monkeys


def part_1():
    monkeys = read_input_file("input.txt")

    round = 1
    while round < 21:
        for nr, monkey in monkeys.items():
            while monkey["items"]:
                old = monkey["items"].pop(0)
                monkey["inspections"] += 1
                new = eval(monkey["operation"])
                worry_level = new // 3
                if worry_level % monkey["test"]["division"]:
                    monkeys[monkey['test']['false']]["items"].append(worry_level)
                else:
                    monkeys[monkey['test']['true']]["items"].append(worry_level)

        # print_round(monkeys, round)
        round += 1

    inspections = list(reversed(sorted([m["inspections"] for m in monkeys.values()])))
    return inspections[0]*inspections[1]


def print_round(monkeys: dict, round: int):
    print(f"After round {round}, the monkeys are holding items with these worry levels:")
    for nr, monkey in monkeys.items():
        print(f"Monkey {nr} ({monkey['inspections']}): {', '.join(str(x) for x in monkey['items'])}")


def part_2():
    monkeys = read_input_file("input.txt")

    round = 1
    while round < 10001:
        for nr, monkey in monkeys.items():
            while monkey["items"]:
                old = monkey["items"].pop(0)
                monkey["inspections"] += 1
                new = eval(monkey["operation"])
                find_common_div = prod(set([m["test"]["division"] for m in monkeys.values()]))
                worry_level = new % find_common_div
                if worry_level % monkey["test"]["division"]:
                    monkeys[monkey['test']['false']]["items"].append(worry_level)
                else:
                    monkeys[monkey['test']['true']]["items"].append(worry_level)
        # print_round(monkeys, round)
        round += 1

    inspections = list(reversed(sorted([m["inspections"] for m in monkeys.values()])))
    return inspections[0] * inspections[1]


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
