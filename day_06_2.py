from functools import reduce

def parse_groups(lines):
    groups = []
    new_group = True
    g = set()
    
    for line in lines:
        if line == "":
            groups.append(g)
            new_group = True
            g = set()
        else:
            p = set()
            for c in line:
                p.add(c)

            if new_group:
                g = p
                new_group = False
            else:
                g = g.intersection(p)
    return groups


file = open('input/day_06_1.txt')
lines = [l.strip() for l in file.readlines()]
file.close()

groups = parse_groups(lines)

print(groups)

count = reduce(lambda c, s: c + len(s), groups, 0)

print(count)

