import re


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return [c for c in content.split("\n")]


def generate_new_password(password: str) -> str:
    for i in range(2):
        is_valid_password = False
        while not is_valid_password:
            # increment password
            r = list(password)[::-1]
            i = 0
            for c in r:
                if c == 'z':
                    r[i] = 'a'
                else:
                    r[i] = chr(ord(c) + 1)
                    break
                i += 1
            password = ''.join(r[::-1])

            # is valid?
            has_straight = False
            for i in range(len(password) - 2):
                if ord(password[i]) == ord(password[i + 1]) - 1 and \
                        ord(password[i]) == ord(password[i + 2]) - 2:
                    has_straight = True
                    break
            if not has_straight:
                continue
            if 'i' in password or 'o' in password or 'l' in password:
                continue
            if len(re.findall(r'(.)\1', password)) < 2:
                continue

            is_valid_password = True
        return password


def part_1(data):
    password = data.pop()
    return generate_new_password(password)


def part_2(data):
    password = data.pop()
    password1 = generate_new_password(password)
    return generate_new_password(password1)


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "11_input.txt"
    data = read_input_file(filepath)
    ans = part_1(data)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "11_input.txt"
    data = read_input_file(filepath)
    ans = part_2(data)
    print(f"answer: {ans}")
