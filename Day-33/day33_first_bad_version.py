# Day 33 - The Defective Robot Factory
# Find the first bad version using binary search.


def is_bad_version(version, first_bad):
    return version >= first_bad


def first_bad_version(total_versions, first_bad):
    left = 1
    right = total_versions

    while left < right:
        mid = left + (right - left) // 2

        if is_bad_version(mid, first_bad):
            right = mid
        else:
            left = mid + 1

    return left


print("----- Defective Robot Factory -----")

total_versions = 20
first_bad = 13

result = first_bad_version(total_versions, first_bad)

print("Total versions:", total_versions)
print("Actual first bad version:", first_bad)
print("Detected first bad version:", result)

print("\nVerification:")
if result == first_bad:
    print("Correct: First bad version detected.")
else:
    print("Incorrect result.")

print("\nComplexity:")
print("Time: O(log N)")
print("Extra Space: O(1)")
