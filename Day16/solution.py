import re
from functools import reduce

rules = {}
my_ticket = None
nearby_tickets = []

input = ""
with open('input.txt') as f:
   input = f.read() 

for group in re.findall('([\w ]+): (\d+-\d+) or (\d+-\d+)', input):
    field, range_1, range_2 = group[0], group[1], group[2]
    rules[field] = ((range_1.split('-')[0], range_1.split('-')[1]), 
            (range_2.split('-')[0], range_2.split('-')[1]))

my_ticket = re.findall('your ticket:\n([\d,]+)' , input)[0].split(',')
my_ticket = list(map(int, my_ticket))

for ticket in re.findall('nearby tickets:\n((?:[\d,]+\n)+)', input)[0].split():
    nearby_tickets.append(ticket.split(','))

# part 1
valid_tickets = [my_ticket]

ranges = [range(int(r[0]), int(r[1])+1) for values in rules.values() for r in values]
sum_ = 0
for ticket in nearby_tickets:
    invalid = False
    for field in ticket:
        if all([int(field) not in r for r in ranges]):
            invalid = True
            sum_ += int(field)
    if not invalid:
        valid_tickets.append(list(map(int, ticket)))
print(sum_)

# part 2
fields_cols = {}
for field, ranges in rules.items():
    ranges = [range(int(r[0]), int(r[1])+1) for r in ranges]
    for col_idx in range(len(my_ticket)):
        column = [ticket[col_idx] for ticket in valid_tickets]
        if all([any([x in r for r in ranges]) for x in column]):
            if field in fields_cols:
                fields_cols[field].append(col_idx)
            else:
                fields_cols[field] = [col_idx]

binding = {}
while any(fields_cols.values()):
    # check if there is a column that can be applied
    # to a specific field only
    for field, columns in fields_cols.items():
        other_fields_columns = [cols for f, cols in fields_cols.items() if f != field]
        other_fields_columns = [item for sublist in other_fields_columns for item in sublist]
        if any([c not in other_fields_columns for c in columns]):
            taken_column = next(c for c in columns if c not in other_fields_columns) 
            binding[field] = taken_column
            # remove taken column
            fields_cols[field] = [c for c in fields_cols[field] if c != taken_column]

    # check if there is a field that has only one column
    for field, columns in fields_cols.items():
        if len(columns) == 1:
            taken_column = columns[0]
            binding[field] = taken_column
            # remove taken column
            for f, c in fields_cols.items():
                fields_cols[f] = [c for c in fields_cols[f] if c != taken_column]

seq = [my_ticket[binding[key]] for key in binding.keys() if key.startswith('departure')]
print(reduce(lambda a,b: a*b, seq))

