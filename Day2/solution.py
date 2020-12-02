with open('input.txt', 'r') as f:
    input = f.readlines()

#first part
valid_passwords = 0
for policy in input:
    allowed_range, letter, password = policy.strip().split(' ')
    letter = letter[0]
    min_number, max_number = map(int, allowed_range.split('-'))

    letter_occurences = password.count(letter)

    if min_number <= letter_occurences <= max_number:
        valid_passwords += 1

print(valid_passwords)

#second part
valid_passwords = 0
for policy in input:
    positions, letter, password = policy.strip().split(' ')
    letter = letter[0]
    first_position, second_position = map(lambda position: int(position) - 1, positions.split('-'))

    if sum([password[first_position] == letter, password[second_position] == letter]) == 1:
        valid_passwords += 1

print(valid_passwords)