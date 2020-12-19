from itertools import product
import regex
import re

input = []
with open('input.txt') as f:
    input = [line.strip() for line in f]

messages = []
rules = {}

for line in input:
    if ':' in line:
        rule, matches = line.split(':')
        rules[rule] = matches.strip().replace('"','')
    elif line:
        messages.append(line)


# part 1
def matches(rule):
    if rules[rule].isalpha():
        return [rules[rule]]

    possibilities = []

    options = [x.strip() for x in rules[rule].split('|')]
    for option in options:
        m = []
        for r in option.split():
            m.append(matches(r))
        m = [''.join(p) for p in list(product(*m))]
        possibilities.extend(m)

    return possibilities

matches_for_zero = matches('0')

print(sum([msg in matches_for_zero for msg in messages]))

#part 2
rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'

def matches_part2(rule):
    if rule == '8':
        return ['(' + '|'.join(matches_part2('42')) + ')+']
    if rule == '11':
        a = '(' + '|'.join(matches_part2('42')) + ')'
        b = '(' + '|'.join(matches_part2('31')) + ')'
        return ['(?:' + '|'.join(f'{a}{{{n}}}{b}{{{n}}}' for n in range(1, 10)) + ')']

    if rules[rule].isalpha():
        return [rules[rule]]

    possibilities = []

    options = [x.strip() for x in rules[rule].split('|')]
    for option in options:
        m = []
        for r in option.split():
            m.append(matches_part2(r))
        m = [''.join(p) for p in list(product(*m))]
        possibilities.extend(m)

    return possibilities

print(sum([1 for msg in messages for rule in matches_part2('0') if re.fullmatch(rule, msg)]))
