s = "anagram"
t = "nagaram"

# Check if both strings have the same length
if len(s) != len(t):
    print("Not an Anagram")
else:
    counts = {}

    # Count characters in the first string
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    # Remove counts using the second string
    for char in t:
        counts[char] = counts.get(char, 0) - 1

    # Check if all counts are zero
    is_anagram = True

    for value in counts.values():
        if value != 0:
            is_anagram = False

    if is_anagram:
        print("Valid Anagram")
    else:
        print("Not an Anagram")
