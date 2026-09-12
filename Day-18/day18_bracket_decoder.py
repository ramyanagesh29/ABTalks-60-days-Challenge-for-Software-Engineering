# Day 18 - Ancient Bracket Decoder

def is_valid_brackets(text):
    stack = []

    matching = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in text:

        # Opening bracket
        if char in "([{":
            stack.append(char)

        # Closing bracket
        elif char in ")]}":

            # No opening bracket available
            if not stack:
                return False

            # Top bracket does not match
            if stack[-1] != matching[char]:
                return False

            # Remove matched opening bracket
            stack.pop()

    # Valid only if nothing is left
    return len(stack) == 0


# Test cases
test_cases = [
    "()",
    "[]",
    "{}",
    "([{}])",
    "{[()]}",
    "([)]",
    "{]",
    "(((",
    "]"
]

print("----- Ancient Bracket Decoder -----")

for text in test_cases:
    if is_valid_brackets(text):
        print(text, "-> Valid")
    else:
        print(text, "-> Invalid")
