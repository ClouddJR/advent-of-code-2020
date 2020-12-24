from llist import dllist, dllistnode

cups = [int(x) for x in '198753462']

current = cups[0]
len_cups = len(cups)
for i in range(100):
    current_idx = cups.index(current)
    c1 = cups[(current_idx + 1) % len_cups]
    c2 = cups[(current_idx + 2) % len_cups]
    c3 = cups[(current_idx + 3) % len_cups]
    cups.remove(c1)
    cups.remove(c2)
    cups.remove(c3)

    dest = current - 1
    min_ = 1 if 1 not in [c1, c2, c3] else min(cups)
    max_ = 9 if 9 not in [c1, c2, c3] else max(cups)
    while dest >= min_:
        if dest in cups:
            dest = cups[cups.index(dest)]
            break
        dest -= 1

    if dest < min_:
        dest = max_

    dest_index = cups.index(dest)
    cups = cups[:dest_index + 1] + [c1, c2, c3] + cups[dest_index + 1:]
    current = cups[(cups.index(current) + 1) % len_cups]

# part 1
final = cups[cups.index(1) + 1:] + cups[:cups.index(1)]
print(''.join(map(str, final)))

# linked list of cups
cups = [int(x) for x in '198753462'] + list(range(10, 1000001))
linked = dllist(cups)

# dictonary- cup label and a reference
d = {}
node = linked.first
while node:
    d[node.value] = node
    node = node.next

current = linked.first
for _ in range(10000000):
    c1 = current.next if current.next else linked.first
    c2 = c1.next if c1.next else linked.first
    c3 = c2.next if c2.next else linked.first

    min_ = 1 if 1 not in [c1.value, c2.value, c3.value] else min(linked)
    max_ = 1000000 if 1000000 not in [c1.value, c2.value, c3.value] else max(linked)

    dest = current.value - 1 if current.value != 1 else max_
    while dest in [c1.value, c2.value, c3.value]:
        dest = dest - 1 if dest != 1 else max_

    dest = d[dest]

    c1 = dllistnode(linked.remove(c1))
    c2 = dllistnode(linked.remove(c2))
    c3 = dllistnode(linked.remove(c3))

    d[c1.value] = c1
    d[c2.value] = c2
    d[c3.value] = c3

    linked.insertnode(c1, dest.next) if dest.next else linked.insertnode(c1)
    linked.insertnode(c2, c1.next) if c1.next else linked.insertnode(c2)
    linked.insertnode(c3, c2.next) if c2.next else linked.insertnode(c3)

    current = current.next if current.next else linked.first

# part 2
print(d[1].next.value * d[1].next.next.value)
