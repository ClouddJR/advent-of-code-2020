import re


def isFieldValid(field):
    name = field[0]
    value = field[1]
    validation_rules = {
        'byr': lambda v: len(v) == 4 and 1920 <= int(v) <= 2002,
        'iyr': lambda v: len(v) == 4 and 2010 <= int(v) <= 2020,
        'eyr': lambda v: len(v) == 4 and 2020 <= int(v) <= 2030,
        'hgt': lambda v: bool(re.match('^((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)$', v)),
        'hcl': lambda v: bool(re.match('^#[a-f0-9]{6}$', v)),
        'ecl': lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda v: len(v) == 9,
        'cid': lambda v: True
    }
    return validation_rules[name](value)


def isPassportValid(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    fields = [field.split(':') for field in passport]
    field_names = [field[0] for field in fields]
    return all([field in field_names for field in required_fields]) and all([isFieldValid(field) for field in fields])


with open('input.txt') as f:
    passports = f.read().split('\n\n')

passports = [passport.split() for passport in passports]
valid_passports = sum([isPassportValid(passport) for passport in passports])

print(valid_passports)
