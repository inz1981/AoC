def read_input_file(path):
    with open(path) as f:
        content = f.read()
        lines = [str(c) for c in content.split("\n")]
        return lines


def get_valid_busses(data):
    busses = data.split(",")
    return [int(bus) for bus in busses if bus != "x"]


def get_valid_busses_inc_no_req(data):
    busses = data.split(",")
    return [bus for bus in busses]


def get_timetable(busses, max_roundtrip, start_time):
    time = 0
    timetable = []
    for bus in busses:
        curr_bus = []
        for time in range(0, max_roundtrip + start_time):
            if time == 0:
                curr_bus.append((bus, time, "D"))
            elif not (time % bus):
                curr_bus.append((bus, time, "D"))
            else:
                curr_bus.append((bus, time, "."))
        timetable.append(curr_bus)
    return timetable


def get_timetable_two(busses, start_time):
    earliest_time = 0
    time = start_time
    bus_idx = 0
    no_busses = len(busses)
    while True:
        bus_no = busses[bus_idx]
        if not time % int(bus_no):
            # print(f"time: {time}")
            bus_idx += 1
            possible_start_time = time
            time += 1
            for bus_idx in range(bus_idx, len(busses)):
                if busses[bus_idx] == "x":
                    time += 1
                elif not time % int(busses[bus_idx]):
                    time += 1
                else:
                    possible_start_time = 0
                    break
            if possible_start_time:
                print(f"FOUND START: {possible_start_time}")
                return possible_start_time
        bus_idx = 0
        time += 1


def get_next_departure(timetable, depart_time):

    # bus_no, waiting_time
    result = []
    for bus in timetable:
        for idx in range(depart_time, len(bus)):
            bus_no, time, status = bus[idx]
            if status == "D":
                if not result:
                    print(f"bus ({bus_no}) departs at {time} which is "
                          f"{time - depart_time} minutes waiting time.")
                    result.insert(0, bus_no)
                    result.insert(1, time - depart_time)
                    break
                elif (time-depart_time) < result[1]:
                    print(f"bus ({bus_no}) departs at {time} which is "
                          f"{time-depart_time} minutes waiting time.")
                    result[0] = bus_no
                    result[1] = time-depart_time
                    break
                else:
                    print(f"bus ({bus_no}) takes too long time to wait: "
                          f"{time-depart_time} minutes.")
                    break
    return result


def part_1(path):
    data = read_input_file(path)

    depart_time = int(data[0])
    valid_busses = get_valid_busses(data[1])
    max_roundtrip = max(valid_busses)
    timetable = get_timetable(valid_busses, max_roundtrip, depart_time)

    next_dep = get_next_departure(timetable, depart_time)
    print(next_dep)
    return next_dep[0] * next_dep[1]


def part_2(path):
    data = read_input_file(path)

    depart_time = int(data[0])
    valid_busses = get_valid_busses_inc_no_req(data[1])
    timetable = get_timetable_two(valid_busses, depart_time)
    print(timetable)
    return timetable


def part__2(path):
    data = read_input_file(path)
    d = 1
    i = 0
    busses = [(i, int(x)) for i, x in enumerate(data[1].split(",")) if x != "x"]

    for offset, bus in busses:
        while True:
            i += d
            if (i + offset) % bus == 0:
                d = d * bus
                break
    return i


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "13_input.txt"
    data = part_1(filepath)
    print(f"answer: {data}")

    print("----- part 2 -----")
    filepath = "13_input.txt"
    data = part_2(filepath)

    print(f"answer: {data}")
