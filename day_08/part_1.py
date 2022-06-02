class State():
    def __init__(self, acc, index):
        self.acc = acc
        self.index = index
        self.running = True


class Instruction():
    def __init__(self, cmd, arg, visited):
        self.cmd = cmd
        self.arg = arg
        self.visited = visited


def parse_line(line):
    halves = line.split(' ')
    cmd = halves[0]
    arg = halves[1]
    arg_int = int(arg[1:]) if arg[:1] == '+' else int(arg[1:]) * -1
    visited = False
    return Instruction(cmd, arg_int, visited)


def execute_program(program):
    state = State(0, 0)
    while state.running:
        i = state.index
        instr = program[i]
        program[i] = execute_instruction(instr, state)


def execute_instruction(instr, state):
    if instr.visited:
        print('Infinite loop! Acc value:', state.acc)
        state.running = False
    elif instr.cmd == 'acc':
        state.acc += instr.arg
        state.index += 1
    elif instr.cmd == 'jmp':
        state.index += instr.arg
    elif instr.cmd == 'nop':
        state.index += 1
    else:
        raise Exception('Unknown operation:', instr.cmd)
    instr.visited = True
    return instr


# Read file
f = open('input.txt')
program = [parse_line(line) for line in f.readlines()]
f.close()

execute_program(program)
