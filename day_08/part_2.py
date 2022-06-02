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

    def change_cmd(self, cmd):
        return Instruction(cmd, self.arg, False)


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
        if i == len(program):
            print("Program Terminated! Acc:", state.acc)
            state.running = False
        else:
            instr = program[i]
            program[i] = execute_instruction(instr, state)


def execute_instruction(instr, state):
    if instr.visited:
        print('loop. acc:', state.acc, "i:", state.index)
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


def try_alternates(program):
    for i in range(len(program)):
        instr = program[i]
        if instr.cmd == 'jmp':
            reset(program)
            alt_program = program[:]
            alt_instr = alt_program[i].change_cmd('nop')
            alt_program[i] = alt_instr
            execute_program(alt_program)

        elif instr.cmd == 'nop':
            reset(program)
            alt_program = program[:]
            alt_instr = alt_program[i].change_cmd('jmp')
            alt_program[i] = alt_instr
            execute_program(alt_program)

def reset(program):
    for instr in program:
        instr.visited = False

# Read file
f = open('input.txt')
program = [parse_line(line) for line in f.readlines()]
f.close()

try_alternates(program)
