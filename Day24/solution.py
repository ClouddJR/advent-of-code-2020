def parse(l):
    result = []
    idx = 0
    while idx < len(l):
        if l[idx] == 'e' or l[idx] == 'w':
            result.append(l[idx])
            idx += 1
        if l[idx:idx+2] == 'se' or l[idx:idx+2] == 'sw' or l[idx:idx+2] == 'nw' or l[idx:idx+2] == 'ne':
            result.append(l[idx:idx+2])
            idx += 2
    return result


input = None

with open('input.txt') as f:
    input = [line.strip() for line in f]
    input = [parse(line) for line in input]


d = {}
for i in input:
    x, y, z = 0, 0, 0
    for dir in i:
        if dir == 'e':
            x, y, z = x + 1, y - 1, z
        if dir == 'w':
            x, y, z = x - 1, y + 1, z
        if dir == 'se':
            x, y, z = x, y - 1, z + 1
        if dir == 'nw':
            x, y, z = x, y + 1, z - 1
        if dir == 'sw':
            x, y, z = x - 1, y, z + 1
        if dir == 'ne':
            x, y, z = x + 1, y, z - 1
    tile = (x, y, z)
    if tile in d:
        d[tile] = d[tile] + 1
    else:
        d[tile] = 1

# part 1
print(sum([d[tile] % 2 == 1 for tile in d]))

d = {tile: (True if flips % 2 == 1 else False) for tile, flips in d.items()}


def get_neighbours():
    neighbours = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                if x + y + z == 0:
                    if x == 0 and y == 0 and z == 0:
                        continue
                    neighbours.append((x, y, z))
    return neighbours


def black_neighbours(tile):
    count = 0
    neighbours = get_neighbours()
    for neighbour in neighbours:
        t = (tile[0] + neighbour[0], tile[1] +
             neighbour[1], tile[2] + neighbour[2])
        if t in d:
            count += 1 if d[t] else 0

    return count


def add_neighbours_of_black(d, blacks):
    for tile in blacks:
        neighbours = get_neighbours()
        for neighbour in neighbours:
            t = (tile[0] + neighbour[0], tile[1] +
                 neighbour[1], tile[2] + neighbour[2])
            if t not in d:
                d[t] = False


for _ in range(100):
    new_d = {}
    add_neighbours_of_black(d, [tile for tile in d if d[tile]])
    for tile, is_black in d.items():
        blacks = black_neighbours(tile)
        if is_black:
            if blacks == 0 or blacks > 2:
                new_d[tile] = False
                continue
        else:
            if blacks == 2:
                new_d[tile] = True
                continue
        new_d[tile] = is_black
    d = new_d

# part2
print(sum([d[tile] for tile in d]))
