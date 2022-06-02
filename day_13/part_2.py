class Bus():
    def __init__(self, bus_id, delay):
        self.bus_id = bus_id
        self.delay = delay


def get_remainders(bus_list):
    timetable = []
    for i in range(len(bus_list)):
        bus = bus_list[i]
        if bus != 'x':
            bus_id = int(bus)
            delay = (bus_id - i) % bus_id
            timetable.append(Bus(bus_id, delay))
    return timetable


def print_timetable(timetable):
    print('Timetable:')
    print('mod, remainder')
    for b in timetable:
        print(b.bus_id, b.delay)
    print()


def get_longest(timetable):
    longest = Bus(0, 0)
    for bus in timetable:
        if bus.bus_id > longest.bus_id:
            longest = bus
    return longest


def find_consecutive_bus_time(timeable):
    longest = timetable[0]
    interval = longest.bus_id
    candidate = longest.delay

    print(candidate, 'for', interval)

    for bus in timetable[1:]:
        remainder = bus.delay % bus.bus_id

        while candidate % bus.bus_id != remainder:
            candidate += interval

        print(candidate, 'for', bus.bus_id)
        interval = interval * bus.bus_id

    print('\nFinal answer:', candidate, 'mod', interval)



f = open('input.txt')
f.readline()
timetable = get_remainders(f.readline().strip().split(','))
timetable = sorted(timetable, key=lambda b: -b.bus_id)
print_timetable(timetable)


find_consecutive_bus_time(timetable)

