import math
from functools import reduce

map = []
with open('input.txt', 'r') as f:
    for line in f:
        map.append(line.strip())


def count_trees_for_slope(right, down, original_map):
    map = original_map.copy()

    # repeat the map to the right
    map_height = len(map)
    required_with = ((map_height//down) * right) + 1
    no_duplication = math.ceil(required_with / len(map[0]))

    for i in range(len(map)):
        map[i] = map[i] * no_duplication

    # calculate the number of trees
    no_trees = 0
    x = 0
    y = 0
    for _ in map:
        x += right
        y += down
        if y >= len(map):
            break
        no_trees += 1 if map[y][x] == '#' else 0

    return no_trees


trees_with_slopes = [
    count_trees_for_slope(1, 1, map),
    count_trees_for_slope(3, 1, map),
    count_trees_for_slope(5, 1, map),
    count_trees_for_slope(7, 1, map),
    count_trees_for_slope(1, 2, map)
]
print(reduce(lambda a, b: a * b, trees_with_slopes))
