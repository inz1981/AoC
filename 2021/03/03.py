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
    oxy = data[::]
    co2 = data[::]

    for x in range(len(oxy[0])):
        num_0 = 0
        num_1 = 0
        for y in range(len(oxy)):
            if oxy[y][x] == "1":
                num_1 += 1
            elif oxy[y][x] == "0":
                num_0 += 1
            else:
                raise ValueError("Don't know what to do.")

        if num_0 > num_1:
            oxy = [g for g in oxy if g[x] == "0"]
        elif num_1 > num_0:
            oxy = [g for g in oxy if g[x] == "1"]
        else:
            oxy = [g for g in oxy if g[x] == "1"]
        if len(oxy) == 1:
            break

    for x in range(len(co2[0])):
        num_0 = 0
        num_1 = 0
        for y in range(len(co2)):
            if co2[y][x] == "1":
                num_1 += 1
            elif co2[y][x] == "0":
                num_0 += 1
            else:
                raise ValueError("Don't know what to do.")

        if num_0 < num_1:
            co2 = [g for g in co2 if g[x] == "0"]
        elif num_1 < num_0:
            co2 = [g for g in co2 if g[x] == "1"]
        else:
            co2 = [g for g in co2 if g[x] == "0"]
        if len(co2) == 1:
            break

    return int(oxy[0], 2)*int(co2[0], 2)


if __name__ == '__main__':
    print("----- part 1 -----")
    part1_ans = part_1()
    print(f"answer: {part1_ans}")

    print("----- part 2 -----")
    part2_ans = part_2()
    print(f"answer: {part2_ans}")
