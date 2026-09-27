# Day 31 - The Dutch Flag Sorting Machine

Sort an array containing only 0, 1, and 2 without built-in sorting.

## Dutch National Flag Algorithm

Use three pointers:
- `low` for the zero region
- `mid` for the current element
- `high` for the two region

If current is 0, swap with low and move low and mid.
If current is 1, move mid.
If current is 2, swap with high and move high. Keep mid in place.

## Complexity

- Time: O(N)
- Extra Space: O(1)
- In-place: Yes
- Built-in sorting: No

## Interview Explanation

"I divide the array into regions for 0, 1, and 2 using three pointers.
Every element is processed a constant number of times, giving O(N)
time and O(1) extra space."
