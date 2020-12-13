from functools import reduce
with open('input.txt') as f:
    time = int(f.readline())
    sequence = [b.strip() for b in f.readline().split(',')]

# part 1
buses = [int(el) for el in sequence if el != 'x']
bus = min(buses, key=lambda bus: bus - time % bus)
print(bus * (bus - time % bus))


def chinese_remainder(n, a):
    sum_ = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum_ += a_i * mul_inv(p, n_i) * p
    return sum_ % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


# part 2
n = buses
a = [(b - sequence.index(str(b))) % b for b in buses]
print(chinese_remainder(n, a))
