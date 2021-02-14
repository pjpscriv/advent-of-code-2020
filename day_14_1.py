def write_memory(lines):
    memory = {}
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        elif line.startswith('mem'):
            index = int(line[line.find('[')+1: line.find(']')])
            number = int(line.split(' = ')[1])
            ones  = int(mask.replace('X', '0'), 2)
            zeros = int(mask.replace('X', '1'), 2)
            number = (number & zeros) | ones
            memory[index] = number
        else:
            raise('Invalid Input!: ' + line)
    
    return memory

f = open('input/day_14.txt')
lines = f.readlines()
f.close()

memory = write_memory(lines)

print('Answer:', sum([memory[i] for i in memory]))
