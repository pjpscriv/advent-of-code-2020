from functools import reduce


def parse_lines(lines):
    active_cubes = set()
    z, w = 0, 0
    for i, line in enumerate(lines):
        y = len(lines) - (i+ 1)
        for x in range(len(line.strip())):
            char = line[x]
            if char == '#':
                active_cubes.add((x, y, z, w))
    return active_cubes


def get_bounding_ranges(hypercubes):
    x_range = list(map(lambda c: c[0], hypercubes))
    y_range = list(map(lambda c: c[1], hypercubes))
    z_range = list(map(lambda c: c[2], hypercubes))
    w_range = list(map(lambda c: c[3], hypercubes))
    return [
        [min(x_range) - 1, max(x_range) + 1],
        [min(y_range) - 1, max(y_range) + 1],
        [min(z_range) - 1, max(z_range) + 1],
        [min(w_range) - 1, max(w_range) + 1]
    ]


def count_active_neighbours(hypercube, active_cubes):
    x0, y0, z0, w0 = hypercube
    neighbours = [(x, y, z, w)
        for x in range(x0-1, x0+2)
        for y in range(y0-1, y0+2)
        for z in range(z0-1, z0+2)
        for w in range(w0-1, w0+2)]
    neighbours.remove(hypercube)
    return reduce(lambda x, c: x+1 if c in active_cubes else x, neighbours, 0)


f = open('input.txt')
lines = f.readlines()
f.close()

active_cubes = parse_lines(lines)
bounds = get_bounding_ranges(active_cubes)


loop = 0
print(f'Loop {loop}. Bounds: {bounds}, Active: {len(active_cubes)}')


while loop < 6:
    next_active_cubes = set()
    for x in range(bounds[0][0], bounds[0][1]+1):
        for y in range(bounds[1][0], bounds[1][1]+1):
            for z in range(bounds[2][0], bounds[2][1]+1):
                for w in range(bounds[3][0], bounds[3][1]+1):
                    hypercube = (x, y, z, w)
                    if hypercube in active_cubes:
                        if 2 <= count_active_neighbours(hypercube, active_cubes) <= 3:
                            next_active_cubes.add(hypercube)
                    else:
                        if count_active_neighbours(hypercube, active_cubes) == 3:
                            next_active_cubes.add(hypercube)
    loop += 1
    active_cubes = next_active_cubes
    bounds = get_bounding_ranges(active_cubes)
    print(f'Loop {loop}. Bounds: {bounds}, Active: {len(active_cubes)}')

