import json


def read_input_file(file_name: str):
    with open(file_name) as f:
        content = f.read()
        newlines = content.split("\n\n")
        return [line.replace("\n", " ") for line in newlines]


def sort_packets(packets):
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for idx in range(len(packets) - 1):
            if not compare_input(packets[idx], packets[idx + 1]):
                tmp = packets[idx]
                packets[idx] = packets[idx + 1]
                packets[idx + 1] = tmp
                has_swapped = True

    return packets


def compare_input(val_left, val_right):
    print(f"- Compare {val_left} vs {val_right}")
    if isinstance(val_left, int) and isinstance(val_right, int):
        if val_left < val_right:
            print("- Left side is smaller, so inputs are in the right order")
            return True
        elif val_left > val_right:
            print("- Right side is smaller, so inputs are not in the right order")
            return False

    elif isinstance(val_left, list) and isinstance(val_right, list):
        for i, vl in enumerate(val_left):
            try:
                vr = val_right[i]
            except IndexError:
                print("- Right side ran out of items, so inputs are not in the right order")
                return False
            comp = compare_input(vl, vr)
            if comp is not None:
                return comp
        if len(val_left) < len(val_right):
            print(f"- Left side ran out of items, so inputs are in the right order")
            return True

    elif isinstance(val_left, list) and isinstance(val_right, int):
        print(f"- Mixed types; convert right to [{val_right}] and retry comparison")
        return compare_input(val_left, [val_right])

    elif isinstance(val_left, int) and isinstance(val_right, list):
        print(f"- Mixed types; convert left to [{val_left}] and retry comparison")
        return compare_input([val_left], val_right)


def part_1():
    dd = read_input_file("input.txt")
    right_orders = []

    for y, d in enumerate(dd):
        print(f"\n== Pair {y+1} ==")
        left, right = d.split(" ")
        left = json.loads(left)
        right = json.loads(right)
        print(f"- Compare {left} vs {right}")
        comp = None
        for i, val_left in enumerate(left):
            try:
                val_right = right[i]
            except IndexError:
                print("- Right side ran out of items, so inputs are not in the right order")
                break
            comp = compare_input(val_left, val_right)
            if comp:
                right_orders.append(y + 1)
                break
            elif comp is False:
                break
        if len(left) < len(right) and comp is None:
            print(f"- Left side ran out of items, so inputs are in the right order")
            right_orders.append(y + 1)

        # print(f"Right Orders: {right_orders}")

    return sum(right_orders)


def part_2():
    dd = read_input_file("input.txt")

    packets = []
    for y, d in enumerate(dd):
        left, right = d.split(" ")
        left = json.loads(left)
        right = json.loads(right)
        packets.append(left)
        packets.append(right)
    packets.extend([[2]])
    packets.extend([[6]])

    sorted_packets = sort_packets(packets)

    divider = []
    for x, p in enumerate(sorted_packets):
        if p in [[2]] or p in [[6]]:
            divider.append(x+1)
    print(divider)

    return divider[0] * divider[1]


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
