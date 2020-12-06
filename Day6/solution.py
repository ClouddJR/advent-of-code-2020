from functools import reduce 

input = []
with open('input.txt') as f:
    input = f.read().split('\n\n')

# part 1
print(sum([len(set("".join(group).replace('\n', ''))) for group in input]))

# #part 2
print(sum([len(reduce(lambda x, y: set(x) & set(y), group.split())) for group in input]))
