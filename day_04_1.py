from functools import reduce

expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def parse_passports(lines):
    passports = []
    pp = {}
    for line in lines:
        if line.strip() == "":
            passports.append(pp)
            pp = {}
        else:
            fields = line.split(' ')
            for field in fields:
                # print('F:', field)
                key_pair = field.split(':')
                key = key_pair[0].strip()
                value = key_pair[1].strip()
                pp[key] = value
    return passports


def is_valid(passport):
    for f in expected_fields:
        if not f in passport.keys():
            return 0
    return 1

file = open('input/day_04.txt')
lines = file.readlines()
file.close()

passports = parse_passports(lines)

valid = reduce(lambda valid_count, pp: valid_count + is_valid(pp), passports, 0)

print(valid)
