def find_next_bus(busses, time):
    shortest_wait = 999999999
    shortest_id = 0
    for bus in busses:
        if bus != 'x':
            bus_id = int(bus)
            wait_time = bus_id - (time % bus_id)
            if wait_time < shortest_wait:
                shortest_wait = wait_time
                shortest_id = bus_id
    return (shortest_id, shortest_wait)



f = open('input.txt')
start_time = int(f.readline())
busses = f.readline().strip().split(',')
f.close()

res = find_next_bus(busses, start_time)

print('ID:', res[0], 'Time:', res[1])
print('Answer:', res[0] * res[1])
