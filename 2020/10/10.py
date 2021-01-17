DP = {}

def read_input_file(path):
    with open(path) as f:
        content = f.read()
        return [int(c) for c in content.split("\n")]


def part_1():
    data = read_input_file("10_input.txt")
    adapters = sorted(data)

    jolts_diff = {1: 0, 2: 0, 3: 0}
    max_jolt = max(adapters) + 3
    for idx in range(len(adapters)):
        if idx == 0:
            adapter_diff = adapters[idx]
            jolts_diff[adapter_diff] += 1
        if idx > len(adapters)-2:
            adapter_diff = max_jolt - adapters[idx]
            jolts_diff[adapter_diff] += 1
            break
        adapter_diff = adapters[idx+1]-adapters[idx]
        jolts_diff[adapter_diff] += 1
    print(jolts_diff)
    return jolts_diff


def r_adapter_perm(adapters):
    result = []
    min_jolt = 0
    max_jolt = max(adapters) + 3
    result.append(min_jolt)
    for i in range(len(adapters)):
        for j in range(1, 4):
            if i + j >= len(adapters):
                continue
            elif adapters[i + j] <= adapters[i] + 3:
                result[i+j] += adapters[i]
            print(j)
        #print(i)
        if i == 0:
            adapter_diff = adapters[i]
        if i > len(adapters) - 2:
            adapter_diff = max_jolt - adapters[i]
            break
        adapter_diff, adapter_diff_2, adapter_diff_3 = 0, 0, 0
        if len(adapters) - 2 > i:
            adapter_diff = adapters[i + 1] - adapters[i]
        if len(adapters) - 3 > i:
            adapter_diff_2 = adapters[i + 2] - adapters[i]
        if len(adapters) - 4 > i:
            adapter_diff_3 = adapters[i + 3] - adapters[i]
        #print(adapter_diff, adapter_diff_2, adapter_diff_3)

    result.append(max_jolt)

    return result


def count_path(adapters):
    jolts = adapters.copy()
    jolts.reverse()
    jolts.append(0)

    n_adapters = len(jolts)
    n_paths = [0 for i in range(n_adapters)]
    n_paths[0] = 1

    for idx in range(n_adapters-1):
        curr = jolts[idx]
        if jolts[idx + 1] in [curr - 1, curr - 2, curr - 3]:
            n_paths[idx + 1] += n_paths[idx]
        if (idx + 2) < n_adapters and jolts[idx + 2] in [curr - 2, curr - 3]:
            n_paths[idx + 2] += n_paths[idx]
        if (idx + 3) < n_adapters and jolts[idx + 3] == curr - 3:
            n_paths[idx + 3] += n_paths[idx]
    return n_paths[-1]

def part_2():
    data = read_input_file("10_input.txt")
    data.insert(0, 0)
    data.append(max(data) + 3)
    adapters = sorted(data)
    min_jolt = 0
    max_jolt = max(adapters) + 3
    print(adapters)
    # adapter_combo = r_adapter_perm(adapters)

    combinations = r_adapter_perm(0, adapters)
    print(DP)
    return combinations


def r_adapter_perm(i, adapters):
    result = 0
    if i == len(adapters) -1:
        return 1
    if i in DP:
        return DP[i]

    for j in range(i + 1, len(adapters)):
        if adapters[j]-adapters[i] <= 3:
            result += r_adapter_perm(j, adapters)
    DP[i] = result
    return result



def load_input(path):
    adapters_list = []
    with open(path) as f:
        for line in f:
            adapters_list.append(int(line))
    return sorted(adapters_list)


if __name__ == '__main__':
    print("----- part 1 -----")
    data = part_1()
    ans = data[1] * data[3]
    print(f"answer: {ans}")

    print("----- part 2 -----")
    data = part_2()

    print(f"answer: {data}")

    data = load_input("10_input.txt")
    print(f"g {count_path(data)}")