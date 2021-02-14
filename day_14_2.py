from re import finditer

MAX_MASK = '1'*36

def get_masks(index, mask):
    if mask.count('X') == 1:
        i = 36 - mask.find('X')

        one = 2**(i-1)
        zero = int(MAX_MASK[:36-i]+'0'+MAX_MASK[37-i:], 2)
        one_index = index | one
        zero_index = index & zero
        
        return [one_index, zero_index]
    else:
        i = 36 - mask.find('X')

        one_index = index | 2**(i-1)
        one_mask  = mask.replace('X', '1', 1)
        
        zero_index = index & int(MAX_MASK[:36-i]+'0'+MAX_MASK[37-i:], 2)
        zero_mask  = mask.replace('X', '0', 1)

        return get_masks(one_index, one_mask) + get_masks(zero_index, zero_mask)


def write_memory(lines):
    memory = {}
    mask = '000000000000000000000000000000000000'
    for line in lines:
        line.strip()
        if line.startswith('mask'):
            mask = line.split(' = ')[1].strip()
        
        elif line.startswith('mem'):
            number = int(line.split(' = ')[1])

            index = int(line[line.find('[')+1: line.find(']')])

            zeros = int(mask.replace('X', '0'), 2)
            index = index | zeros

            masks = get_masks(index, mask)
            for m in masks:
                memory[m] = number
        else:
            raise('Invalid Input!: ' + line)
    return memory


f = open('input/day_14.txt')
lines = f.readlines()
f.close()

memory = write_memory(lines)

print('Answer:', sum([memory[i] for i in memory]))
