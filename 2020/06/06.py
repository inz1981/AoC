def read_input_file(path):
    with open(path) as f:
        content = f.read()
        newlines = content.split("\n\n")
        groups = [line.replace("\n", " ") for line in newlines]
        return ["".join(set(answers.split())) for answers in groups]


def read_input_file_2(path):
    with open(path) as f:
        content = f.read()
        newlines = content.split("\n\n")
        groups = [line.split("\n") for line in newlines]
        result = 0
        for group in groups:
            g_result = set()
            for group_answer in group:
                for person_answer in group_answer:
                    matches = [a for a in group if person_answer in a]
                    if len(matches) == len(group):
                        g_result.update(person_answer)
            result += len(g_result)
    return result


def part_1():
    data = read_input_file("06_input.txt")
    result = 0
    for d in data:
        result = result + len(set(d))
    return result


def part_2():
    return read_input_file_2("06_input.txt")


if __name__ == '__main__':
    print("----- part 1 -----")
    result = part_1()
    print(f"answer: {result}")

    print("----- part 2 -----")
    result = part_2()
    print(f"answer: {result}")

