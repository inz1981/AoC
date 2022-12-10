import re


def read_input_file(file_name: str):
    with open(file_name) as f:
        """Each line as string."""
        content = f.readlines()
        return [x.strip() for x in content]


def part_1():
    d = read_input_file("input.txt")

    addx_cycles = get_x_cycles(d)

    regx = 1
    signal_strenghts = {
        20: 1,
        60: 0,
        100: 0,
        140: 0,
        180: 0,
        220: 0,
    }
    for x, c in addx_cycles:
        if c < 20:
            regx += x
            signal_strenghts[20] = 20 * regx
        elif c < 60:
            regx += x
            signal_strenghts[60] = 60 * regx
        elif c < 100:
            regx += x
            signal_strenghts[100] = 100 * regx
        elif c < 140:
            regx += x
            signal_strenghts[140] = 140 * regx
        elif c < 180:
            regx += x
            signal_strenghts[180] = 180 * regx
        elif c < 220:
            regx += x
            signal_strenghts[220] = 220 * regx

    return sum(signal_strenghts.values())


def get_x_cycles(d):
    addx_cycles = []
    for cycle, cmd in enumerate(d):
        if cmd == "noop":
            if not addx_cycles:
                addx_cycles.append([0, cycle + 1])
            else:
                lastcmd, last_cycle = addx_cycles[-1]
                addx_cycles.append([0, last_cycle + 1])
        else:
            addx = int(re.findall(r"addx ([+-]?\d+(?:\.\d+)?)", cmd)[0])
            if not addx_cycles:
                addx_cycles.append([addx, cycle + 2])
            else:
                lastcmd, last_cycle = addx_cycles[-1]
                addx_cycles.append([addx, last_cycle + 2])
    return addx_cycles


def part_2():
    d = read_input_file("input.txt")
    addx_cycles = get_x_cycles(d)

    regx = 1
    cycle_str = ""
    for cycle in range(0, 240):
        row_cycle = cycle % 40
        cycle += 1
        next_x, on_cycle = addx_cycles[0]
        sprite = list(range(regx - 1, regx + 2))
        if row_cycle in sprite:
            cycle_str += "#"
        else:
            cycle_str += "."
        if on_cycle == cycle:
            regx += next_x
            addx_cycles.pop(0)

    current_x = 0
    for x in range(0, len(cycle_str)):
        if not x == 0 and not x % 40:
            print(cycle_str[current_x:x])
            current_x = x
    print(cycle_str[current_x:])

    return "see printout above."


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
