def two_sum(nums, target):
    seen = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index
    return None

if __name__ == "__main__":
    nums, target = [2, 7, 11, 15], 9
    print("Array:", nums)
    print("Target:", target)
    print("Indices:", two_sum(nums, target))
