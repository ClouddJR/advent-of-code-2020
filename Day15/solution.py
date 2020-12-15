input = [9, 19, 1, 6, 0, 5, 4]


def solve(max_round):
    previous = {x: i + 1 for i, x in enumerate(input)}

    last = input[-1]
    for r in range(len(input) + 1, max_round + 1):
        current = r - 1 - previous[last] if last in previous else 0
        previous[last] = r - 1
        last = current

    print(last)

solve(2020)
solve(30000000)
