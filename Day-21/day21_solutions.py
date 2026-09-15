# Day 21 - Forbidden Functions Tournament

# Puzzle 1 - Recursive Factorial

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


number = 5

factorial_result = factorial(number)

print("----- Puzzle 1: Recursive Factorial -----")
print("Number:", number)
print("Factorial:", factorial_result)
