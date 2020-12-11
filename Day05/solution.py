boarding_passes = []
with open('input.txt') as f:
    for line in f:
        boarding_passes.append(line.strip())

# part 1
seat_ids = []
for boarding_pass in boarding_passes:
    rows = [i for i in range(128)]
    columns = [i for i in range(8)]

    for row in boarding_pass[:7]:
        rows = rows[len(rows)//2:] if row == 'B' else rows[:len(rows)//2]
    for column in boarding_pass[7:]:
        columns = columns[len(columns)//2:] if column == 'R' else columns[:len(columns)//2]

    seat_ids.append(int(rows[0]) * 8 + int(columns[0]))

print(max(seat_ids))

# part 2
print([seat for seat in range(min(seat_ids), max(seat_ids) + 1) if seat not in seat_ids][0])
