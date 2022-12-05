import re


def read_input_file(file_name: str):
    with open(file_name) as f:
        content = f.read()
        crates, commands = content.split("\n\n")

        commands = commands.split("\n")
        crates = crates.split("\n")

        c_stack = []
        stack_str = crates[-1]

        for x in range(0, int(re.findall(r'\d+', stack_str)[-1])):
            c_stack.append([])

        for t in crates:
            p = re.compile("([A-Z]+)")
            for q in p.finditer(t):
                crate = q.group()
                pos = q.start()
                stack_nr = stack_str[pos]
                # print(f"{crate} goes to stack: {stack_nr}")
                c_stack[int(stack_nr)-1].append(crate)
        return c_stack, commands


def part_1():
    crate_stack, commands = read_input_file("input.txt")

    for command in commands:
        num_crate, from_c, to_c = re.findall(r"move (\d+) from (\d+) to (\d+)", command)[0]
        for i in range(0, int(num_crate)):
            crate_stack[int(to_c)-1].insert(0, crate_stack[int(from_c)-1].pop(0))

    ans = ""
    for crate in crate_stack:
        if crate:
            ans += crate[0]

    return ans


def part_2():
    crate_stack, commands = read_input_file("input.txt")

    for command in commands:
        num_crate, from_c, to_c = re.findall(r"move (\d+) from (\d+) to (\d+)", command)[0]
        moves = []
        for i in range(0, int(num_crate)):
            moves.append(crate_stack[int(from_c)-1].pop(0))

        for move in reversed(moves):
            crate_stack[int(to_c) - 1].insert(0, move)

    ans = ""
    for crate in crate_stack:
        if crate:
            ans += crate[0]

    return ans


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
