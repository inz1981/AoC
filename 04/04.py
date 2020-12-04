import re


def read_input_file(path):
    with open(path) as f:
        content = f.read()
        newlines = content.split("\n\n")
        passports = [line.replace("\n", " ") for line in newlines]
        return passports


def read_input_file_part2(path, req_keys):
    with open(path) as f:
        content = f.read()
        newlines = content.split("\n\n")
        passports = [line.replace("\n", " ") for line in newlines]
        check_passports = list()
        for passport in passports:
            checked_passport = extended_check(passport, req_keys)
            if checked_passport:
                check_passports.append(checked_passport)
        return check_passports


def extended_check(passport, req_keys):
    byr = re.findall(r"byr:([0-9]{4})", passport)
    iyr = re.findall(r"iyr:([0-9]{4})", passport)
    hcl = re.findall(r"hcl:#([0-9a-f]{6})", passport)
    ecl = re.findall(r"ecl:([a-z]{3})", passport)
    eyr = re.findall(r"eyr:([0-9]{4})", passport)
    pid = re.findall(r"pid:([\d]+)", passport)
    hgt = re.findall(r"hgt:([\d]{2,3})([a-z]{2})", passport)
    if not byr or (int(byr[0]) < 1920 or int(byr[0]) > 2002):
        return None
    if not iyr or (int(iyr[0]) < 2010 or int(iyr[0]) > 2020):
        return None
    if not eyr or (int(eyr[0]) < 2020 or int(eyr[0]) > 2030):
        return None
    if not hgt or not hgt[0][1] in ["in", "cm"]:
        return None
    if hgt[0][1] == "cm" and (int(hgt[0][0]) < 150 or int(hgt[0][0]) > 193):
        return None
    if hgt[0][1] == "in" and (int(hgt[0][0]) < 59 or int(hgt[0][0]) > 76):
        return None
    if not hcl:
        return None
    if not pid or (len(pid[0]) != 9):
        return None
    if not ecl or not any(m in ecl[0] for m in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        return None
    return passport


if __name__ == '__main__':
    req_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    print("----- part 1 -----")
    data = read_input_file("04/04_input.txt")
    pass_keys = list()
    for d in data:
        matching = [s for s in req_keys if s in d]
        pass_keys.append(matching)
    valid_passports = 0
    for pass_key in pass_keys:
        if pass_key == req_keys:
            valid_passports = valid_passports + 1

    print(f"valid passports: {valid_passports}")

    print("----- part 2 -----")
    data = read_input_file_part2("04/04_input.txt", req_keys)
    print(f"valid passports: {len(data)}")

