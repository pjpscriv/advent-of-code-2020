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

def parse_fields(lines):
    fields = []
    for line in lines:
        if not ':' in line:
            break
        fields.append(Field(line))
    return fields


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



f = open('input.txt')
lines = f.readlines()
f.close()

fields = parse_fields(lines)
tickets = parse_nearby_tickets(lines)

invalid_values = []

for ticket in tickets:
    for value in ticket:
        is_invalid = True
        for f in fields:
            if f.is_valid(value):
                is_invalid = False
                break
        if is_invalid:
            invalid_values.append(value)

print(f'Error Rate: {sum(invalid_values)}')
