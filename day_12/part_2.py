DIRS = ['N', 'E', 'S', 'W']

class State():
    def __init__(self):
        self.way_x = 10
        self.way_y = 1
        self.x = 0
        self.y = 0


def parse_com(com):
    return (com[0], int(com[1:]))


def update_waypoint(state, action, val):
    if action == 'N':
        state.way_y = state.way_y + val
    elif action == 'E':
        state.way_x = state.way_x + val
    elif action == 'S':
        state.way_y = state.way_y - val
    elif action == 'W':
        state.way_x = state.way_x - val
    else:
        raise Exception('Unknown direction: '+action)

def rotate_waypoint(state, action, val):
    for _ in range(val // 90):
        if action == 'R':
            new_way_x = state.way_y
            new_way_y = state.way_x * -1
            state.way_x = new_way_x
            state.way_y = new_way_y
        else:
            new_way_x = state.way_y * -1
            new_way_y = state.way_x
            state.way_x = new_way_x
            state.way_y = new_way_y


def update_position(state, val):
    state.x = state.x + (state.way_x * val)
    state.y = state.y + (state.way_y * val)


def execute(instr, state):
    action = instr[0]
    val = instr[1]
    if action in ['N', 'E', 'S', 'W']:
        update_waypoint(state, action, val)
    elif action in ['R', 'L']:
        rotate_waypoint(state, action, val)
    elif action == 'F':
        update_position(state, val)
    else:
        raise Exception('Unknown command: '+com[0])


f = open('input.txt')
commands = [parse_com(line.strip()) for line in f.readlines()]
f.close()

s = State()

for com in commands:
    execute(com, s)

manhattan = abs(s.x) + abs(s.y)

print('Dist:', manhattan)

# print(s.way_x, s.way_y)
# rotate_waypoint(s, 'L', 180)
# print(s.way_x, s.way_y)
# rotate_waypoint(s, 'R', 180)
# print(s.way_x, s.way_y)
