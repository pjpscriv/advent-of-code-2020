from functools import reduce


def parse_line(line):
    line = line.split(':')
    rule = line[0].split(' ')
    limits = rule[0].split('-')

    min_limit = int(limits[0])
    max_limit = int(limits[1])
    letter = rule[1]
    pwd = line[1].strip()
    
    return (min_limit, max_limit, letter, pwd)


def count_valid(line_tuple):
    min_limit, max_limit, letter, pwd = line_tuple
    count = pwd.count(letter)

    if count >= min_limit and count <= max_limit:
        return 1
    else:
        return 0


file = open('input/day_02.txt')
nums = [parse_line(x) for x in file.readlines()]
file.close()

valid = reduce(lambda x, y: x + count_valid(y), nums, 0)

print(valid)
