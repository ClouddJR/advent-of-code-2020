from enum import Enum

seats = []
with open('input.txt') as f:
    for line in f:
        seats.append(list(line.strip()))

seats_p1 = seats
seats_p2 = seats.copy()

empty = 'L'
floor = '.'
occ = '#'
rows = len(seats_p1)
cols = len(seats_p1[0])

# part 1
diff = True
while diff:
    new = [[0] * cols for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            current = seats_p1[row][col]
            row_start = max(row - 1, 0)
            row_end = min(row + 1, rows - 1)
            col_start = max(col - 1, 0)
            col_end = min(col + 1, cols - 1)

            adj = [seat for c in seats_p1[row_start:row_end + 1] for seat in c[col_start:col_end + 1]]
            adj.remove(current)

            if current == empty and all([seat != occ for seat in adj]):
                new[row][col] = occ
            elif current == occ and sum([seat == occ for seat in adj]) >= 4:
                new[row][col] = empty
            else:
                new[row][col] = current

    diff = new != seats_p1
    seats_p1 = new

print(sum([' '.join(map(str, row)).count(occ) for row in seats_p1]))

# part 2


class Direction(Enum):
    TOP = (-1, 0)
    TOP_RIGHT = (-1, 1)
    RIGHT = (0, 1)
    BOTTOM_RIGHT = (1, 1)
    BOTTOM = (1, 0)
    LEFT_BOTTOM = (1, -1)
    LEFT = (0, -1)
    TOP_LEFT = (-1, -1)


def in_bounds(row, col):
    return 0 <= row < rows and 0 <= col < cols


def get_first(arr, row, col, direction):
    dy = direction.value[0]
    dx = direction.value[1]
    while in_bounds(row + dy, col + dx):
        row += dy
        col += dx
        if arr[row][col] == empty:
            return empty
        elif arr[row][col] == occ:
            return occ
    return ''


diff = True
while diff:
    new = [[0] * cols for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            current = seats_p2[row][col]
            occupied = sum([get_first(seats_p2, row, col, d) == occ for d in Direction])

            if current == empty and occupied == 0:
                new[row][col] = occ
            elif current == occ and occupied >= 5:
                new[row][col] = empty
            else:
                new[row][col] = current

    diff = new != seats_p2
    seats_p2 = new

print(sum([' '.join(map(str, row)).count(occ) for row in seats_p2]))
