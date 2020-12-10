from itertools import takewhile
from functools import reduce

adapters = []
with open('input.txt') as f:
    adapters = [int(line.strip()) for line in f]

# part 1
ordered = [0] + sorted(adapters) + [max(adapters) + 3]
diff = {}
for i in range(len(ordered) - 1):
    d = ordered[i + 1] - ordered[i]
    diff[d] = diff.get(d, 0) + 1

print(diff[1] * diff[3])

# part 2 -dynamic programming
cache = {}
def dp(i):
    if i == len(ordered) - 1:
        return 1
    if i in cache:
        return cache[i]
    ans = 0
    for j in range(i + 1, min(i + 4, len(ordered))):
         if ordered[j] - ordered[i] <= 3:
            ans += dp(j)
    cache[i] = ans
    return ans

print(dp(0))
