from functools import reduce


def parse_line(line):
    line = line.split(':')
    rule = line[0].split(' ')
    limits = rule[0].split('-')

    pos_1 = int(limits[0])
    pos_2 = int(limits[1])
    letter = rule[1]
    pwd = line[1].strip()
    
    return (pos_1, pos_2, letter, pwd)


def count_valid(line_tuple):
    pos_1, pos_2, letter, pwd = line_tuple

    if pwd[pos_1-1] == letter and pwd[pos_2-1] == letter:
        return 0
    if pwd[pos_1-1] != letter and pwd[pos_2-1] != letter:
        return 0
    else:
        return 1


file = open('input/day_02.txt')
nums = [parse_line(x) for x in file.readlines()]
file.close()

valid = reduce(lambda x, y: x + count_valid(y), nums, 0)

print(valid)
