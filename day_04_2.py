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


def valid_birth_year(val):
    year = int(val)
    return 1920 <= year <= 2002 

def valid_issue_year(val):
    year = int(val)
    return 2010 <= year <= 2020 

def valid_exp_year(val):
    year = int(val)
    return 2020 <= year <= 2030


def valid_height(val):
    if val.endswith('cm'):
        h = int(val[:-2])
        return 150 <= h <= 193
    elif val.endswith('in'):
        h = int(val[:-2])
        return 59 <= h <= 76
    else:
        return False

def valid_hair(val):
    if len(val) != 7 or val[0] != '#':
        return False
    for c in val[1:]:
        if not (c.isnumeric() or c in 'abcdef'):
            return False
    return True

def valid_eyes(val):
    return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_passport(val):
    return len(val) == 9 and val.isnumeric()


validators = {
    'byr': valid_birth_year,
    'iyr': valid_issue_year,
    'eyr': valid_exp_year,
    'hgt': valid_height,
    'hcl': valid_hair,
    'ecl': valid_eyes,
    'pid': valid_passport
}


def is_valid(passport):
    for f in expected_fields:
        if not f in passport.keys():
            return 0
        else:
            value = passport[f]
            valid = validators[f]
            if not valid(value):
                return 0
    return 1


file = open('input/day_04.txt')
lines = file.readlines()
file.close()

passports = parse_passports(lines)

valid = reduce(lambda valid_count, pp: valid_count + is_valid(pp), passports, 0)

print(valid)
