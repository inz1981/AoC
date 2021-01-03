import re


def read_input_file(path):
    with open(path) as f:
        content = f.read()
    replacements, molecule = [c for c in content.split("\n\n")]
    replacements = [c for c in replacements.split("\n")]
    repl_dict = {}
    electrons = {}
    for repl in replacements:
        v1, v2 = re.findall("(.*) => (.*)", repl).pop()
        if v1 == "e":
            if v1 not in electrons:
                electrons[v1] = [v2]
            else:
                electrons[v1].append(v2)
        elif v1 not in repl_dict:
            repl_dict[v1] = [v2]
        else:
            repl_dict[v1].append(v2)
    return repl_dict, electrons, molecule


def nth_repl(s, sub, repl, n):
    find = s.find(sub)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != n:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == n:
        return s[:find] + repl + s[find+len(sub):]
    return s


def part_1(path):
    replacements, _, molecule = read_input_file(path)

    print(replacements, molecule)

    result_mols = []
    for repl, values in replacements.items():
        num_occ = molecule.count(repl)
        for occ in range(1, num_occ+1):
            for val in values:
                result_mols.append(nth_repl(molecule, repl, val, occ))
    ans = len(set(result_mols))

    return replacements, ans


def get_replacements_options(molecule: str, replacements: dict):
    rkeys = list(replacements.keys())
    match = re.findall("([A-Z][a-z]|[A-Z])", molecule)
    return [{m: replacements[m]} for m in match if m in rkeys]


def part_2(filepath):
    replacements = []
    with open(filepath) as fh:
        d = fh.readlines()
        molecule = d[-1].strip()
        for l in d[:-2]:
            replacements.append(l.strip().split(" => "))
    replacements_copy = replacements.copy()

    num_replacements = 0
    current_molecule = molecule
    while current_molecule != 'e':
        try:
            f = max(replacements, key=lambda x: len(x[1]))
        except ValueError:
            replacements = replacements_copy.copy()
            f = max(replacements, key=lambda x: len(x[1]))
        before, after = f
        replaced_molecule = current_molecule.replace(after, before, 1)
        if current_molecule != replaced_molecule:
            num_replacements += 1
        else:
            replacements.remove(f)
        current_molecule = replaced_molecule
        # print(current_molecule)

    return num_replacements


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "19_input.txt"
    repl, ans = part_1(filepath)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "19_input.txt"
    ans = part_2(filepath)
    print(f"answer: {ans}")
