from functools import reduce

def parse_groups(lines):
    groups = []
    g = set()
    for line in lines:
        if line == "":
            groups.append(g)
            g = set()
        else:
            for c in line:
                g.add(c)
    return groups


file = open('input/day_06_1.txt')
lines = [l.strip() for l in file.readlines()]
file.close()

groups = parse_groups(lines)

count = reduce(lambda c, s: c + len(s), groups, 0)

print(count)
