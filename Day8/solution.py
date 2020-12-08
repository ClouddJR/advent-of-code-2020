instructions = []
with open('input.txt') as f:
    instructions = [line.strip().split() for line in f]
    instructions = [(operator, int(argument)) for operator, argument in instructions]


def process(instructions):
    acc = 0
    visited = set()
    current_idx = 0
    while (current_idx not in visited) and current_idx < len(instructions):
        visited.add(current_idx)
        operation, argument = instructions[current_idx]
        if operation == 'nop':
            current_idx += 1
        if operation == 'acc':
            acc += argument
            current_idx += 1
        if operation == 'jmp':
            current_idx += argument

    # value of accumulator and whether instructions were correct
    return acc, current_idx not in visited


# part 1
print(process(instructions)[0])

# part 2
for index, instruction in enumerate(instructions):
    operation, argument = instruction
    if operation == 'acc':
        continue
    new_operation = 'jmp' if operation == 'nop' else 'nop'
    instructions_copy = instructions.copy()
    instructions_copy[index] = (new_operation, instructions[index][1])
    acc, correct = process(instructions_copy)
    if correct:
        print(acc)
        break
