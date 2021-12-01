def read_input_file(file_name: str):
    with open(file_name) as f:
        return [int(x) for x in f]


def part_1():
    sonars = read_input_file("input.txt")

    increases = 0
    for idx, depth in enumerate(sonars):
        if idx == 0:
            continue
        if sonars[idx-1] < depth:
            increases += 1
    return increases


def part_2():
    sonars = read_input_file("input.txt")

    prev = 0
    increases = 0
    for i in range(1, len(sonars)):
        if sum(sonars[i:i+3]) > prev:
            increases += 1
        prev = sum(sonars[i:i+3])
    return increases


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
