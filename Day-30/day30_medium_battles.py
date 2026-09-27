def longest_unique_substring(text):
    last_seen = {}
    left = 0
    best_length = 0
    best_start = 0

    for right, char in enumerate(text):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right

        if right - left + 1 > best_length:
            best_length = right - left + 1
            best_start = left

    return text[best_start:best_start + best_length]


def product_except_self(numbers):
    result = [1] * len(numbers)

    prefix = 1
    for i in range(len(numbers)):
        result[i] = prefix
        prefix *= numbers[i]

    suffix = 1
    for i in range(len(numbers) - 1, -1, -1):
        result[i] *= suffix
        suffix *= numbers[i]

    return result


print("===== Hacker Tournament Finals =====")
text = "abcabcbb"
print("\nBattle 1: Longest Unique Substring")
print("Input:", text)
answer = longest_unique_substring(text)
print("Longest substring:", answer)
print("Length:", len(answer))

numbers = [1, 2, 3, 4]
print("\nBattle 2: Product of Array Except Self")
print("Input:", numbers)
print("Output:", product_except_self(numbers))

print("\nComplexity:")
print("Battle 1: O(N) time, O(N) space")
print("Battle 2: O(N) time, O(N) output space, O(1) extra space")
