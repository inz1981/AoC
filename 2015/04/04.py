import hashlib


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return content


def part_1(data):
    i = 0
    while True:
        md5sum = hashlib.md5(f"{data}{i}".encode('utf-8')).hexdigest()
        if md5sum.startswith("00000"):
            break
        i += 1
    return i


def part_2(data):
    i = 0
    while True:
        md5sum = hashlib.md5(f"{data}{i}".encode('utf-8')).hexdigest()
        if md5sum.startswith("000000"):
            try:
                int(md5sum[6])
                break
            except ValueError:
                print(f"{md5sum} contains no number on pos 7")
        i += 1
    return i


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "04_input.txt"
    data = read_input_file(filepath)
    ans = part_1(data)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "04_input.txt"
    data = read_input_file(filepath)
    ans = part_2(data)
    print(f"answer: {ans}")
