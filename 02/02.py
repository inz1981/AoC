import itertools


def tax_calc(data: list, wanted_sum: int, combos):
    for numbers in itertools.combinations(data, combos):
        if sum(numbers) == wanted_sum:
            return [data.index(number) for number in numbers]


def read_input_file():
    with open('02/02_input.txt') as f:
        content = f.readlines()
        return [x.strip() for x in content]


def get_input_data(data: list):
    result = list()
    for ent in data:
        split_line = ent.split(" ")
        split_line[1] = split_line[1].replace(":", "")
        result.append(split_line)
    return result


def count_char(char: str, password: str):
    return password.count(char)


def correct_passw(data: list):
    result = list()
    for ent in data:
        num_occ = count_char(ent[1], ent[2])
        interval = ent[0].split("-")
        if int(interval[0]) <= num_occ <= int(interval[1]):
            result.append(ent)
    return result


def check_char(char: str, password: str, positions: list):
    if (password[positions[0]-1] == char or password[positions[1]-1] == char) and \
            count_char(char, password[positions[0]-1]+password[positions[1]-1]) == 1:
        return True
    return False


def correct_passw_2(data: list):
    result = list()
    for ent in data:
        interval = list(map(int, ent[0].split("-")))
        if check_char(ent[1], ent[2], interval):
            result.append(ent)
    return result


if __name__ == '__main__':

    input_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    input_data = read_input_file()

    print("----- part 1 -----")
    data = get_input_data(input_data)
    correct_pwds = correct_passw(data)
    print(f"Correct passwords: {len(correct_pwds)}")

    print("----- part 2 -----")
    data = get_input_data(input_data)
    correct_pwds = correct_passw_2(data)
    print(f"Correct passwords: {len(correct_pwds)}")
