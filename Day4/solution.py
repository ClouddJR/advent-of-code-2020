import re


def isFieldValid(field):
    name = field[0]
    value = field[1]
    if name == 'byr':
        return len(value) == 4 and 1920 <= int(value) <= 2002
    elif name == 'iyr':
        return len(value) == 4 and 2010 <= int(value) <= 2020
    elif name == 'eyr':
        return len(value) == 4 and 2020 <= int(value) <= 2030
    elif name == 'hgt':
        return re.match('^((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)$', value) != None
    elif name == 'hcl':
        return re.match('^#[a-f0-9]{6}$', value) != None
    elif name == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif name == 'pid':
        return len(value) == 9
    elif name == 'cid':
        return True

    return False


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
