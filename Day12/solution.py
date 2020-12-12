import math

with open('input.txt') as f:
    instructions = [line.strip() for line in f]


# part 1
directions = ['N', 'E', 'S', 'W']
facing = 'E'
x = 0
y = 0


def move(direction, units):
    global x, y
    if direction == 'N':
        y += units
    elif direction == 'S':
        y -= units
    elif direction == 'E':
        x += units
    elif direction == 'W':
        x -= units


def change_facing(direction, degrees):
    global facing
    degress = 360 % degrees
    if direction == 'R':
        facing = directions[(directions.index(facing) +
                             degrees % 360//90) % len(directions)]
    else:
        facing = directions[(directions.index(facing) -
                             degrees % 360//90) % len(directions)]


for i in instructions:
    action = i[0]
    val = int(i[1:])

    if action == 'F':
        move(facing, val)
    elif action == 'N':
        move('N', val)
    elif action == 'S':
        move('S', val)
    elif action == 'E':
        move('E', val)
    elif action == 'W':
        move('W', val)
    elif action == 'R':
        change_facing('R', val)
    elif action == 'L':
        change_facing('L', val)

print(abs(x) + abs(y))

# part 2
sx, sy = 0, 0
wx, wy = 10, 1


def move_waypoint(direction, units):
    global wx, wy
    if direction == 'N':
        wy += units
    elif direction == 'S':
        wy -= units
    elif direction == 'E':
        wx += units
    elif direction == 'W':
        wx -= units


def rotate_waypoint(direction, degrees):
    global wx, wy
    degrees = math.radians(degrees)
    s = math.sin(degrees)
    c = math.cos(degrees)
    if direction == 'R':
        newx = round(wx * c + wy * s)
        newy = round(-wx * s + wy * c)
    elif direction == 'L':
        newx = round(wx * c - wy * s)
        newy = round(wx * s + wy * c)
    wx = newx
    wy = newy


def move_ship(value):
    global wx, wx, sx, sy
    sx += wx * value
    sy += wy * value


for i in instructions:
    action = i[0]
    val = int(i[1:])

    if action == 'F':
        move_ship(val)
    elif action == 'N':
        move_waypoint('N', val)
    elif action == 'S':
        move_waypoint('S', val)
    elif action == 'E':
        move_waypoint('E', val)
    elif action == 'W':
        move_waypoint('W', val)
    elif action == 'R':
        rotate_waypoint('R', val)
    elif action == 'L':
        rotate_waypoint('L', val)

print(abs(sx) + abs(sy))
