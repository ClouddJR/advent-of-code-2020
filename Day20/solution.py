import numpy as np
import re
from functools import reduce

tiles = None
with open('input.txt') as f:
    tiles = f.read().split('\n\n')
    tiles = [x.strip() for x in tiles if x]
    tiles = [(x.split(':\n')[0].split(' ')[1], x.split(':\n')[1])
             for x in tiles]
    tiles = [(id, x.split('\n')) for id, x in tiles]

sides_map = {}
for id, tile in tiles:
    side1 = tile[0]
    side2 = tile[-1]
    side3 = ''.join([row[0] for row in tile])
    side4 = ''.join([row[-1] for row in tile])
    sides = [side1, side2, side3, side4]

    for s in sides:
        if s in sides_map:
            sides_map[s].append(id)
        else:
            sides_map[s] = [id]

        rev = s[::-1]

        if rev in sides_map:
            sides_map[rev].append(f'{id}-r')
        else:
            sides_map[rev] = [f'{id}-r']

corners = set()
for side, ids in sides_map.items():
    if len(ids) == 1 and '-r' not in ids[0] and list(sides_map.values()).count(ids) > 1:
        corners.add(ids[0])

# part 1
print(reduce(lambda a, b: int(a) * int(b), corners))


tiles_map = {id: np.array([[char for char in row]
                           for row in tile]) for id, tile in tiles}


def transformations(tile):
    for k in [0, 1, 2, 3]:
        yield np.rot90(tile, k=k)
    for axis in [0, 1]:
        for k in [0, 1]:
            yield np.rot90(np.flip(tile, axis=axis), k=k)


def assemble(t, t_id, x, y, image):
    image[(x, y)] = (t_id, t)

    if (x - 1, y) not in image:
        ts = ''.join(t[0, :])
        t_matches = [s.replace('-r', '')
                     for s in sides_map[ts] if t_id not in s]
        if t_matches:
            for tf in transformations(tiles_map[t_matches[0]]):
                bs = ''.join(tf[-1, :])
                if bs == ts:
                    assemble(tf, t_matches[0], x - 1, y, image)
                    break
    if (x, y + 1) not in image:
        rs = ''.join(t[:, -1])
        r_matches = [s.replace('-r', '')
                     for s in sides_map[rs] if t_id not in s]
        if r_matches:
            for tf in transformations(tiles_map[r_matches[0]]):
                ls = ''.join(tf[:, 0])
                if ls == rs:
                    assemble(tf, r_matches[0], x, y + 1, image)
                    break
    if (x + 1, y) not in image:
        bs = ''.join(t[-1, :])
        b_matches = [s.replace('-r', '')
                     for s in sides_map[bs] if t_id not in s]
        if b_matches:
            for tf in transformations(tiles_map[b_matches[0]]):
                ts = ''.join(tf[0, :])
                if ts == bs:
                    assemble(tf, b_matches[0], x + 1, y, image)
                    break
    if (x, y - 1) not in image:
        ls = ''.join(t[:, 0])
        l_matches = [s.replace('-r', '')
                     for s in sides_map[ls] if t_id not in s]
        if l_matches:
            for tf in transformations(tiles_map[l_matches[0]]):
                rs = ''.join(tf[:, -1])
                if rs == ls:
                    assemble(tf, l_matches[0], x, y - 1, image)
                    break


def connect(image):
    x, y = max(image)
    rows = []
    for r in range(x + 1):
        row = []
        for c in range(y + 1):
            row.append(image[(r, c)][1][1:9, 1:9])
        rows.append(np.hstack(row))
    return np.vstack((rows))


image = {}

tl_id = next(iter(corners))
for t in transformations(tiles_map[tl_id]):
    rs = ''.join(t[:, -1])
    bs = ''.join(t[-1, :])
    r_matches = [s.replace('-r', '') for s in sides_map[rs] if tl_id not in s]
    b_matches = [s.replace('-r', '') for s in sides_map[bs] if tl_id not in s]
    if r_matches and b_matches:
        assemble(t, tl_id, 0, 0, image)
        break


connected = connect(image)

pattern = '.{18}#.#.{4}##.{4}##.{4}###.#..#..#..#..#..#.{3}'
positions = [19, 21, 26, 27, 32, 33, 38, 39, 40, 42, 45, 48, 51, 54, 57]
win_x = 3
win_y = 20
for tf in transformations(connected):
    x, y = tf.shape
    found = False
    for r in range(x + 1 - win_x):
        for c in range(y + 1 - win_y):
            window = tf[r:r+win_x, c:c+win_y]
            window = "".join(["".join(row) for row in window])
            m = re.fullmatch(pattern, window)
            if m:
                found = True
                temp = list(m.string)
                for p in positions:
                    temp[p - 1] = 'O'
                tf[r:r+win_x, c:c+win_y] = np.array(temp).reshape(win_x, win_y)
    if found:
        break

# part 2
print(sum(["".join(row).count('#') for row in tf]))
