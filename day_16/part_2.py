class Field:
    name = ""
    ranges = []

    def __init__(self, line):
        name, range_string = line.split(':')
        self.name = name

        range_string = range_string.strip()
        pairs = range_string.split(' or ')
        self.ranges = [[int(x) for x in p.split('-')] for p in pairs]

    def __str__(self):
        return f'{self.name}: {self.ranges}'

    def __repr__(self):
        return self.__str__()

    def is_valid(self, value):
        for range in self.ranges:
            if min(range) <= value and value <= max(range):
                return True
        return False


class PostionMap:
    map = {}

    def __init__(self, fields):
        for i in range(len(fields)):
            self.map[i] = [f.name for f in fields]

    def __repr__(self):
        repr = ''
        for k in self.map.keys():
            repr += f'{k}:{self.map[k]}\n'
        return repr

    def keys(self):
        return self.map.keys()

    def fields(self, i):
        return self.map[i]

    def remove(self, name, i):
        names = self.map[i]

        if name in names:
            names.remove(name)
            if len(names) == 0:
                raise Exception(f'No possible fields remaing for position {i}')
            self.map[i] = names

            if len(names) == 1:
                final_name = names[0]
                for j in self.keys():
                    if j != i:
                        self.remove(final_name, j)
        return names

    def get_departure_product(self, ticket):
        departure_filter = lambda k: 'departure' in self.map[k][0]
        indicies = list(filter(departure_filter, self.keys()))
        product = 1
        for i in indicies:
            product *= ticket[i]
        return product


def parse_fields(lines):
    fields = []
    for line in lines:
        if not ':' in line:
            break
        fields.append(Field(line))
    return fields


def parse_my_ticket(lines):
    index = lines.index('your ticket:\n')
    return [int(x) for x in lines[index+1].split(',')]


def parse_nearby_tickets(lines):
    tickets = []
    parsing_on = False
    for line in lines:
        if not parsing_on:
            if 'nearby tickets:' in line:
                parsing_on = True
        else:
            tickets.append([int(x) for x in line.split(',')])
    return tickets


def filter_valid_tickets(tickets, fields):
    valid_tickets = []
    for ticket in tickets:
        if all([any([f.is_valid(value) for f in fields]) for value in ticket]):
            valid_tickets.append(ticket)
    return valid_tickets


f = open('input.txt')
lines = f.readlines()
f.close()


fields = parse_fields(lines)
my_ticket = parse_my_ticket(lines)
tickets = parse_nearby_tickets(lines)
tickets = filter_valid_tickets(tickets, fields)
tickets.append(my_ticket)


field_map = {}
for f in fields:
    field_map[f.name] = f


position_map = PostionMap(fields)


for i in position_map.keys():
    for ticket in tickets:
        value = ticket[i]
        possible_fields = position_map.fields(i)

        for name in possible_fields:
            field = field_map[name]

            if not field.is_valid(value):
                possible_fields = position_map.remove(name, i)


print(position_map)

print(f'Answer: {position_map.get_departure_product(my_ticket)}')
