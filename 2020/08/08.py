import re


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return content.split("\n")


def parse_op(data_str):
    operation = re.findall(r"([a-z]{3}) ([\+|\-]\d+)", data_str)
    return operation[0][0], int(operation[0][1])


def part_2(data):
    i = 0
    for idx, val in enumerate(data):
        data_try = data.copy()
        operation, argument = parse_op(data_try[i])
        if operation == "jmp":
            data_try[idx] = data_try[idx].replace("jmp", "nop")
            if run(data_try):
                print(f"Successful execution when changing operation: "
                      f"{operation} {argument} on pos: {i}")

        if operation == "nop":
            data_try[idx] = data_try[idx].replace("nop", "jmp")
            if run(data_try):
                print(f"Successful execution when changing operation: "
                      f"{operation} {argument} on pos: {i}")
        i += 1


def run(data):
    pos = []
    j = 0
    accumulator = 0
    last_op = len(data)
    while j < last_op:
        if j in pos:
            return 0
        else:
            pos.append(j)
        operation, argument = parse_op(data[j])
        if operation == "nop":
            j += 1
        if operation == "jmp":
            j = j + argument
        if operation == "acc":
            accumulator = accumulator + argument
            j += 1
    print(f"Found it! Accumulator is set to: {accumulator}, pos is: {j}")
    return accumulator


if __name__ == '__main__':
    data = read_input_file("08_input.txt")

    accumulator = 0
    i = 0
    pos = []
    while True:
        if i in pos:
            break
        else:
            pos.append(i)
        operation, argument = parse_op(data[i])
        if operation == "nop":
            i += 1
        if operation == "jmp":
            i = i + argument
        if operation == "acc":
            accumulator = accumulator + argument
            i += 1

    print("----- part 1 -----")
    print(f"accumulator: {accumulator}")

    print("----- part 2 -----")
    part_2(data)
