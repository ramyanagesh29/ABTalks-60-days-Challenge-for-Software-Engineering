import time


# Recursive solution
def climb_recursive(n):
    if n == 0:
        return 1

    if n == 1:
        return 1

    return climb_recursive(n - 1) + climb_recursive(n - 2)


# Optimized solution using memoization
def climb_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n == 0:
        return 1

    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = climb_memo(n - 1, memo) + climb_memo(n - 2, memo)

    return memo[n]


# Test value
n = 10

# Recursive timing
start = time.time()
recursive_result = climb_recursive(n)
end = time.time()

recursive_time = end - start


# Memoization timing
start = time.time()
memo_result = climb_memo(n)
end = time.time()

memo_time = end - start


print("----- Infinite Staircase Puzzle -----")
print("Number of steps:", n)

print("\nRecursive Solution:")
print("Number of ways:", recursive_result)
print("Execution time:", recursive_time)

print("\nMemoization Solution:")
print("Number of ways:", memo_result)
print("Execution time:", memo_time)
