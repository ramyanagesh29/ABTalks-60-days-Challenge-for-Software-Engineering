def sort_colors(numbers):
    low = 0
    mid = 0
    high = len(numbers) - 1

    while mid <= high:
        if numbers[mid] == 0:
            numbers[low], numbers[mid] = numbers[mid], numbers[low]
            low += 1
            mid += 1
        elif numbers[mid] == 1:
            mid += 1
        else:
            numbers[mid], numbers[high] = numbers[high], numbers[mid]
            high -= 1

    return numbers


numbers = [2, 0, 2, 1, 1, 0]

print("----- Dutch Flag Sorting Machine -----")
print("Original:", numbers)
sort_colors(numbers)
print("Sorted:", numbers)
print("\nComplexity:")
print("Time: O(N)")
print("Extra Space: O(1)")
print("Built-in sorting: Not used")
