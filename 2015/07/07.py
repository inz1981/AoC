import re


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return [c for c in content.split("\n")]


def parse_data(data):
    circuit_signals = {}
    incomplete_signals = {}
    for d in data:
        bitlogic, output_wire = d.split(" -> ")
        try:
            signal = int(bitlogic)
            circuit_signals[output_wire] = signal
        except ValueError as e:
            incomplete_signals[output_wire] = bitlogic
    return circuit_signals, incomplete_signals


def part_1(data):

    complete, incomplete = parse_data(data)
    output_incomplete = len(incomplete)
    while output_incomplete:

        for output in list(incomplete):
            logic = incomplete[output]
            operator_and = re.findall("(.*) AND (.*)", logic)
            operator_or = re.findall("(.*) OR (.*)", logic)
            operator_lshift = re.findall("(.*) LSHIFT (\d+)", logic)
            operator_rshift = re.findall("(.*) RSHIFT (\d+)", logic)
            operator_not = re.findall("NOT (.*)", logic)
            no_op = operator_and + operator_or + operator_lshift + operator_rshift + operator_not
            if not no_op:
                input1 = logic
                if input1 in complete:
                    complete[output] = complete[input1]
                    del incomplete[output]

            if operator_and:
                input1, input2 = operator_and.pop()
                try:
                    input1_int = int(input1)
                    if input2 in complete:
                        complete[output] = input1_int & complete[input2]
                        del incomplete[output]
                except ValueError:
                    pass
                if input1 in complete and input2 in complete:
                    complete[output] = complete[input1] & complete[input2]
                    del incomplete[output]
            elif operator_or:
                input1, input2 = operator_or.pop()
                if input1 in complete and input2 in complete:
                    complete[output] = complete[input1] | complete[input2]
                    del incomplete[output]
            elif operator_lshift:
                input1, input2 = operator_lshift.pop()
                if input1 in complete:
                    complete[output] = complete[input1] << int(input2)
                    del incomplete[output]
            elif operator_rshift:
                input1, input2 = operator_rshift.pop()
                if input1 in complete:
                    complete[output] = complete[input1] >> int(input2)
                    del incomplete[output]
            elif operator_not:
                input1 = operator_not.pop()
                if input1 in complete:
                    complete[output] = ~complete[input1] + (65535+1)
                    del incomplete[output]

            output_incomplete = len(incomplete)

    return complete


def part_2(data):
    return data


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "07_input.txt"
    data = read_input_file(filepath)

    ans = part_1(data)
    print(f"answer: {ans['a']}")

    print("----- part 2 -----")
    filepath = "07_input_b_mod.txt"
    data = read_input_file(filepath)
    ans = part_1(data)
    print(f"answer: {ans['a']}")
