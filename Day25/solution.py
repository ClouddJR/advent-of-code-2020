card_public = 5290733
door_public = 15231938
subject = 7

card_value = 1
card_loop_size = 0
while card_value != card_public:
    card_loop_size += 1
    card_value *= subject
    card_value = card_value % 20201227

door_value = 1
door_loop_size = 0
while door_value != door_public:
    door_loop_size += 1
    door_value *= subject
    door_value = door_value % 20201227

subject = card_value
key = 1
for _ in range(door_loop_size):
    key *= subject
    key = key % 20201227
print(key)