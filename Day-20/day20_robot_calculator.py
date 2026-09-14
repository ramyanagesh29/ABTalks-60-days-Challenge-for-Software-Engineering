# Day 20 - Robot Calculator Arena
# Reverse Polish Notation Evaluator


def evaluate_rpn(tokens):

    stack = []

    for token in tokens:

        # If token is a number
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))

        else:
            second = stack.pop()
            first = stack.pop()

            if token == "+":
                result = first + second

            elif token == "-":
                result = first - second

            elif token == "*":
                result = first * second

            elif token == "/":
                # Truncate toward zero
                result = int(first / second)

            stack.append(result)

    return stack[-1]


# Test cases

test_cases = [
    ["2", "3", "+"],
    ["5", "2", "+", "3", "*"],
    ["4", "13", "5", "/", "+"],
    ["10", "6", "-", "2", "*"]
]


print("----- Robot Calculator Arena -----")

for expression in test_cases:

    result = evaluate_rpn(expression)

    print("Expression:", " ".join(expression))
    print("Result:", result)
    print()
