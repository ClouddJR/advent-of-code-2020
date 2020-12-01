numbers = []
with open('input.txt', 'r') as file:
    for line in file:
        numbers.append(int(line.strip()))

for first in numbers:
    for second in numbers:
        for third in numbers:
            if first + second + third == 2020:
                print(first * second * third)
