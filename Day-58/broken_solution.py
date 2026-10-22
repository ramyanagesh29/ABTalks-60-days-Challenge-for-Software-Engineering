# Intentionally broken: range goes one index too far.
def contains_duplicate(nums):
    seen = set()
    for i in range(len(nums) + 1):
        if nums[i] in seen:
            return True
        seen.add(nums[i])
    return False

print(contains_duplicate([1, 2, 3, 2]))
