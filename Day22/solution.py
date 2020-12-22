from queue import Queue

with open('input.txt') as f:
    input = f.read()
    p1, p2 = input.split('\n\n')
    p1 = [int(p) for p in p1.split('\n')[1:] if p]
    p2 = [int(p) for p in p2.split('\n')[1:] if p]

p1q = Queue()
p2q = Queue()

for card in p1:
    p1q.put(card)

for card in p2:
    p2q.put(card)

while not p1q.empty() and not p2q.empty():
    p1c = p1q.get()
    p2c = p2q.get()
    if p1c > p2c:
        p1q.put(p1c)
        p1q.put(p2c)
    else:
        p2q.put(p2c)
        p2q.put(p1c)

winning_deck = p1q if not p1q.empty() else p2q

cards = []
while not winning_deck.empty():
    cards.append(winning_deck.get())

#part 1
print(sum([(index + 1) * card for index, card in enumerate(reversed(cards))]))


def recursiveCombat(p1, p2):
    previous = set()

    while p1 and p2:
        if (tuple(p1), tuple(p2)) in previous:
            return True

        previous.add((tuple(p1), tuple(p2)))

        p1c = p1.pop(0)
        p2c = p2.pop(0)

        if len(p1) >= p1c and len(p2) >= p2c:
            p1_won = recursiveCombat(p1[:p1c], p2[:p2c])
            if p1_won:
                p1.append(p1c)
                p1.append(p2c)
            else:
                p2.append(p2c)
                p2.append(p1c)
        else:
            if p1c > p2c:
                p1.append(p1c)
                p1.append(p2c)
            else:
                p2.append(p2c)
                p2.append(p1c)

    return True if p1 else False

# part 2
recursiveCombat(p1, p2)
print(sum([(index + 1) * card for index, card in enumerate(reversed(p1))]))
