

def read_input():
    return 3029, 2947


def part_1():
    x_target, y_target = read_input()
    x = 1
    y = 1
    code = 20151125

    while x != x_target or y != y_target:
        if y == 1:
            y = x + 1
            x = 1
        else:
            x += 1
            y -= 1

        code = (code*252533) % 33554393
    return code


def part_2():
    weights = read_input()
    return 1


if __name__ == '__main__':
    print("----- part 1 -----")
    ans = part_1()
    print(f"answer: {ans}")

    print("----- part 2 -----")
    ans = part_2()
    print(f"answer: {ans}")
