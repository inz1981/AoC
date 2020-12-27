def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return [c for c in content.split("\n")]


def part_1(data):
    naughty_combo = ["ab", "cd", "pq", "xy"]
    vowels = "aeiou"
    nice_strings = []
    for check_string in data:
        if any(naughty for naughty in naughty_combo if naughty in check_string):
            continue
        vowels_no = 0
        duplicate_letters = 0
        for idx, char in enumerate(check_string):
            if idx:
                prev_char = check_string[idx-1]
                if prev_char == char:
                    duplicate_letters += 1
            if char in vowels:
                vowels_no += 1
        if vowels_no > 2 and duplicate_letters:
            nice_strings.append(check_string)
    return len(nice_strings)


def part_2(data):
    nice_strings = []
    for check_string in data:
        consecutive_letters = 0
        one_between = 0
        for idx, char in enumerate(check_string):
            if idx:
                prev_char = check_string[idx-1]
                check_letters = prev_char+char
                matches = check_string.count(check_letters)
                if matches > 1:
                    consecutive_letters += matches-1
                if idx > 1:
                    prev_prev_char = check_string[idx-2]
                    if prev_prev_char == char:
                        one_between += 1
        if consecutive_letters and one_between:
            nice_strings.append(check_string)
    return len(nice_strings)


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "05_input.txt"
    data = read_input_file(filepath)
    ans = part_1(data)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "05_input.txt"
    data = read_input_file(filepath)
    ans = part_2(data)
    print(f"answer: {ans}")
