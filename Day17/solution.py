import numpy as np
import collections

input = None
with open('input.txt') as f:
    input = [line.strip() for line in f]

#part 1
space = np.array([list(cubes) for cubes in input])
space = space[:, :, np.newaxis]  # covert to 3d

for i in range(0, 6):
    space = np.pad(space, ((1, 1), (1, 1), (1, 1)), constant_values='.')
    new_space = np.copy(space)

    for x in range(space.shape[0]):
        for y in range(space.shape[1]):
            for z in range(space.shape[2]):
                active_neighbors = 0
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        for k in [-1, 0, 1]:
                            if i == 0 and j == 0 and k == 0:
                                continue
                            if 0 <= x+i < space.shape[0] and 0 <= y+j < space.shape[1] and 0 <= z+k < space.shape[2]:
                                if space[x+i][y+j][z+k] == '#':
                                    active_neighbors += 1

                previous = space[x][y][z]
                new_space[x][y][z] = '.' if previous == '#' and active_neighbors not in [
                    2, 3] else '#' if previous == '.' and active_neighbors == 3 else previous
    space = new_space

print(sum([1 for x in space for y in x for z in y if z == '#']))


#part 2
space = np.array([list(cubes) for cubes in input])
space = space[:, :, np.newaxis, np.newaxis]  # covert to 4d
for i in range(0, 6):
    space = np.pad(space, ((1, 1), (1, 1), (1, 1), (1, 1)), constant_values='.')
    new_space = np.copy(space)
    for x in range(space.shape[0]):
        for y in range(space.shape[1]):
            for z in range(space.shape[2]):
                for w in range(space.shape[3]):
                    active_neighbors = 0
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            for k in [-1, 0, 1]:
                                for l in [-1, 0, 1]:
                                    if i == 0 and j == 0 and k == 0 and l == 0:
                                        continue
                                    if 0 <= x+i < space.shape[0] and 0 <= y+j < space.shape[1] and 0 <= z+k < space.shape[2] and 0 <= w+l < space.shape[3]:
                                        if space[x+i][y+j][z+k][w+l] == '#':
                                            active_neighbors += 1
                    previous = space[x][y][z][w]
                    new_space[x][y][z][w] = '.' if previous == '#' and active_neighbors not in [
                        2, 3] else '#' if previous == '.' and active_neighbors == 3 else previous
    space = new_space

print(sum([1 for x in space for y in x for z in y for w in z if w == '#']))