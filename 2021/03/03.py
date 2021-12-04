import collections


def read_input_file(file_name: str):
    with open(file_name) as f:
        """Each line as string."""
        content = f.readlines()
        return [x.strip() for x in content]


def inverse_bin(bits):
    result = ""
    for bit in bits:
        if bit == "1":
            result += "0"
        elif bit == "0":
            result += "1"
        else:
            raise ValueError("What..?")
    return result


def part_1():
    gamma = read_input_file("input.txt")

    most, least = get_most_least_sig(gamma)
    return int(most, 2)*int(least, 2)


def get_most_least_sig(gamma):
    bit_len = len(gamma[0])
    nr_gammas = len(gamma)
    most = ""
    for i in range(0, bit_len):
        nr_zeros = 0
        nr_ones = 0
        for j in range(0, nr_gammas):
            binary = int(gamma[j][i])
            if int(binary):
                nr_ones += 1
            else:
                nr_zeros += 1
        if nr_zeros > nr_ones:
            most += "0"
        elif nr_ones > nr_zeros:
            most += "1"
        else:
            raise NotImplementedError("What?")
    least = inverse_bin(most)
    return most, least


def part_2():
    data = read_input_file("input.txt")
    gamma = data[::]
    for i in range(len(data[0])):
        most = collections.Counter([r[i] for r in gamma])
        most = '1' if most['1'] >= most['0'] else '0'
        gamma = list(filter(lambda x: x[i] == most, gamma))
        if len(gamma) == 1:
            break

    epsilon = data[::]
    for i in range(len(data[0])):
        least = collections.Counter([r[i] for r in epsilon])
        least = '0' if least['1'] >= least['0'] else '1'
        epsilon = list(filter(lambda x: x[i] == least, epsilon))
        if len(epsilon) == 1:
            break

    epsilon_rate = int(epsilon[0], 2)
    gamma_rate = int(gamma[0], 2)
    return gamma_rate * epsilon_rate


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
