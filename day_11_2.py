def check_direction(state, x, y, x_inc, y_inc):
    max_x = len(state[y])
    max_y = len(state)
    x_val = x + x_inc
    y_val = y + y_inc
    value = '.'
    while 0 <= x_val < max_x and 0 <= y_val < max_y and value == '.':
        value = state[y_val][x_val]
        x_val = x_val + x_inc
        y_val = y_val + y_inc
    return value


def no_neighbours(state, x, y):
    for x_inc in [-1, 0, 1]:
        for y_inc in [-1, 0, 1]:
            if not (x_inc == 0 and y_inc == 0):
                val = check_direction(state, x, y, x_inc, y_inc)
                if val == '#':
                    return False
    return True


def five_or_more_neighbours(state, x, y):
    count = 0
    for x_inc in [-1, 0, 1]:
        for y_inc in [-1, 0, 1]:
            if not (x_inc == 0 and y_inc == 0):
                val = check_direction(state, x, y, x_inc, y_inc)
                if val == '#':
                    count += 1
    return count >= 5


def next_state(state):
    changes = 0
    new_state = []
    for row in range(len(state)):
        new_row = ''
        for col in range(len(state[row])):
            val = state[row][col]
            if val == '.':
                new_row += '.'
            elif val == 'L':
                if no_neighbours(state, col, row):
                    new_row += '#'
                    changes += 1
                else:
                    new_row += 'L' 
            elif val == '#':
                if five_or_more_neighbours(state, col, row):
                    new_row += 'L'
                    changes += 1
                else:
                    new_row += '#'
            else:
                raise Exception('Unexpected value:', val)
        new_state.append(new_row)
    return (new_state, changes)


def count_occupied(state):
    count = 0
    for row in state:
        for seat in row:
            if seat == '#':
                count += 1
    return count


f = open('input/day_11.txt')
state = [line.strip() for line in f.readlines()]
f.close()


changes = 100
while changes > 0:
    state, changes = next_state(state)
    print('Changes:', changes)
print('Finished!')
print(count_occupied(state))
