import bisect

def longest_increasing_subsequence(nums):
    tails = []
    for value in nums:
        index = bisect.bisect_left(tails, value)
        if index == len(tails):
            tails.append(value)
        else:
            tails[index] = value
    return len(tails)

if __name__ == "__main__":
    values = [10, 9, 2, 5, 3, 7, 101, 18]
    print("Dynamic programming challenge: LIS")
    print("Input:", values)
    print("Longest increasing subsequence length:", longest_increasing_subsequence(values))
