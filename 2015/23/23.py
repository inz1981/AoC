import re


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        content = [c for c in content.split("\n")]

    result = []

    for line in content:
        data = line.split(", ")
        cmd, op = re.findall(r"(.*) ([a-z]|-\d+|\+\d+)", data[0]).pop()
        cmd_add = [cmd, op]
        if cmd == "jio" or cmd == "jie":
            cmd_add.append(int(data[1]))
        elif cmd == "jmp":
            cmd_add[1] = int(cmd_add[1])
        result.append(cmd_add)

    return result


def part_1_2(path, part_b):
    commands = read_input_file(path)
    if part_b:
        a = 1
    else:
        a = 0
    b = 0

    idx = 0
    while True:

        # print(idx, a, b)
        try:
            curr_command = commands[idx]
        except IndexError as err:
            print(f"We are done (idx: {idx}). a, b: {a, b}")
            return b

        if curr_command[0] == "hlf":
            if curr_command[1] == "a":
                a = int(a/2)
            elif curr_command[1] == "b":
                b = int(b/2)
        elif curr_command[0] == "tpl":
            if curr_command[1] == "a":
                a = a * 3
            elif curr_command[1] == "b":
                b = b * 3
        elif curr_command[0] == "inc":
            if curr_command[1] == "a":
                a += 1
            elif curr_command[1] == "b":
                b += 1
        elif curr_command[0] == "jmp":
            idx += curr_command[1]
            continue

        elif curr_command[0] == "jie":
            if curr_command[1] == "a":
                if not a % 2:
                    idx += curr_command[2]
                    continue
            elif curr_command[1] == "b":
                if not b % 2:
                    idx += curr_command[2]
                    continue
        elif curr_command[0] == "jio":
            if curr_command[1] == "a":
                if a == 1:
                    idx += curr_command[2]
                    continue
            elif curr_command[1] == "b":
                if b == 1:
                    idx += curr_command[2]
                    continue
        idx += 1


def part_2(path):
    commands = read_input_file(path)
    return commands


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "23_input.txt"
    ans = part_1_2(filepath, part_b=False)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "23_input.txt"
    ans = part_1_2(filepath, part_b=True)
    print(f"answer: {ans}")
