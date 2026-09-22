import time


def two_sum_brute_force(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return None


def two_sum_hashmap(numbers, target):
    seen = {}

    for i, number in enumerate(numbers):
        complement = target - number

        if complement in seen:
            return [seen[complement], i]

        seen[number] = i

    return None


numbers = [2, 7, 11, 15, 3, 6]
target = 9

print("----- Lost Treasure Coordinates -----")
print("Numbers:", numbers)
print("Target:", target)

start = time.perf_counter()
brute_result = two_sum_brute_force(numbers, target)
brute_time = time.perf_counter() - start

start = time.perf_counter()
hash_result = two_sum_hashmap(numbers, target)
hash_time = time.perf_counter() - start

print("\nBrute-Force Solution:")
print("Indices:", brute_result)
print("Values:", numbers[brute_result[0]], "+", numbers[brute_result[1]])
print("Execution time:", brute_time)

print("\nHash Map Solution:")
print("Indices:", hash_result)
print("Values:", numbers[hash_result[0]], "+", numbers[hash_result[1]])
print("Execution time:", hash_time)

print("\nComplexity Comparison:")
print("Brute Force: O(N^2) time, O(1) extra space")
print("Hash Map: O(N) average time, O(N) extra space")
