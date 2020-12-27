def no_neighbours(state, x, y):
    max_x = len(state[y]) - 1
    max_y = len(state) - 1
    # Check row above
    if y > 0 and '#' in state[y-1][max(0,x-1):x+2]:
        return False
    # Check row below
    if y < max_y and '#' in state[y+1][max(0,x-1):x+2]:
        return False
    # Check left
    if x > 0 and state[y][x-1] == '#':
        return False
    # Check right
    if x < max_x and state[y][x+1] == '#':
        return False
    # All good
    return True


def four_or_more_neighbours(state, x, y):
    max_x = len(state[y]) - 1
    max_y = len(state) - 1
    count = 0
    # Check row above
    if y > 0:
        for v in state[y-1][max(0,x-1):x+2]:
            if v == '#':
                count += 1
    # Check row below
    if y < max_y:
        for v in state[y+1][max(0,x-1):x+2]:
            if v == '#':
                count += 1
    # Check left
    if x > 0 and state[y][x-1] == '#':
        count += 1
    # Check right
    if x < max_x and state[y][x+1] == '#':
        count += 1
    # Check count
    return count >= 4



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
                if four_or_more_neighbours(state, col, row):
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
    print('Change:', changes)
print('Finished!')
print(count_occupied(state))
