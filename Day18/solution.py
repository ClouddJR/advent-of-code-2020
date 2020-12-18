from collections import deque


def convert_to_rpn(expr):
    out = ""
    stack = deque()
    for char in expr:
        if char.isnumeric():
            out += char
        else:
            if char == '*':
                while stack and stack[-1] != '(':
                    out += stack.pop()
                stack.append(char)
            elif char == '+':
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                popped = stack.pop()
                while popped != '(':
                    out += popped
                    popped = stack.pop()

    while stack:
        out += stack.pop()
    return out


def calculate(rpn):
    stack = deque()
    for char in rpn:
        if char.isnumeric():
            stack.append(char)
        elif char == '*' or char == '+':
            a = int(stack.pop())
            b = int(stack.pop())
            r = a * b if char == '*' else a + b
            stack.append(r)
    return stack.pop()


input = []
with open('input.txt') as f:
    input = [line.strip().replace(' ', '')  for line in f]


results = []
for expression in input:
    rpn = convert_to_rpn(expression)
    results.append(calculate(rpn))


print(sum(results))
