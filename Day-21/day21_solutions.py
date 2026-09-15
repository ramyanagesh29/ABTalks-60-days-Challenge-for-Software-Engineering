# Day 21 - The Forbidden Functions Tournament


# ==========================================
# Puzzle 1 - Recursive Factorial
# ==========================================

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


number = 5

factorial_result = factorial(number)

print("----- Puzzle 1: Recursive Factorial -----")
print("Number:", number)
print("Factorial:", factorial_result)


# ==========================================
# Puzzle 2 - Reverse String Using Stack
# ==========================================

def reverse_using_stack(text):

    stack = []

    for character in text:
        stack.append(character)

    reversed_text = ""

    while stack:
        reversed_text += stack.pop()

    return reversed_text


text = "hello"

reversed_result = reverse_using_stack(text)

print("\n----- Puzzle 2: Stack String Reversal -----")
print("Original:", text)
print("Reversed:", reversed_result)
