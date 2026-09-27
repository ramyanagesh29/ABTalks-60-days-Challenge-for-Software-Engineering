def linear_search(numbers, target):
    for i, number in enumerate(numbers):
        if number == target:
            return i
    return -1


def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


numbers = [3, 8, 12, 17, 21, 25, 31, 42, 56, 63, 70]
target = 42

print("----- Hidden Number Vault -----")
print("Sorted vault:", numbers)
print("Target:", target)

print("\nLinear Search:")
print("Index:", linear_search(numbers, target))

print("\nBinary Search:")
print("Index:", binary_search(numbers, target))

print("\nComplexity Comparison:")
print("Linear Search: O(N) time")
print("Binary Search: O(log N) time")
print("Iterative binary search extra space: O(1)")
