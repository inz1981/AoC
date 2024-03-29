def read_input_file(file_name: str):
    with open(file_name) as f:
        """Each line as string."""
        # content = f.readlines()
        # return [x.strip() for x in content]

        """Multi-line data separated with one empty line."""
        # content = f.read()
        # newlines = content.split("\n\n")
        # return [line.replace("\n", " ") for line in newlines]

        """Each line as integer."""
        return [int(x) for x in f]


def part_1():
    return read_input_file("input.txt")


def part_2():
    return read_input_file("input.txt")


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
