DIRS = ['N', 'E', 'S', 'W']

class State():
    def __init__(self):
        self.rot = 1
        self.x = 0
        self.y = 0


def parse_com(com):
    return (com[0], int(com[1:]))


def update_position(state, action, val):
    if action == 'N':
        state.y = state.y + val
    elif action == 'E':
        state.x = state.x + val
    elif action == 'S':
        state.y = state.y - val
    elif action == 'W':
        state.x = state.x - val
    else:
        raise Exception('Unknown direction: '+action)


def execute(instr, state):
    action = instr[0]
    val = instr[1]
    if action in ['N', 'E', 'S', 'W']:
        update_position(state, action, val)
    elif action in ['R', 'L']:
        mult = -1 if action == 'L' else 1
        state.rot = state.rot + (mult * (val // 90))
    elif action == 'F':
        direction = DIRS[state.rot % 4]
        update_position(state, direction, val)
    else:
        raise Exception('Unknown command: '+com[0])


f = open('input/day_12.txt')
commands = [parse_com(line.strip()) for line in f.readlines()]
f.close()

s = State()

for com in commands:
    execute(com, s)

manhattan = abs(s.x) + abs(s.y)

print('Dist:', manhattan)
