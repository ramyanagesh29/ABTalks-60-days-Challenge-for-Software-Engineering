def contains_duplicate(nums):
    seen = set()
    for value in nums:
        if value in seen:
            return True
        seen.add(value)
    return False

if __name__ == "__main__":
    print("[1, 2, 3, 2] ->", contains_duplicate([1, 2, 3, 2]))
    print("[1, 2, 3, 4] ->", contains_duplicate([1, 2, 3, 4]))
    print("[] ->", contains_duplicate([]))
