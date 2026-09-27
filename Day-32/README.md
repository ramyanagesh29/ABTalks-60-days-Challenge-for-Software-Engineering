# Day 32 - The Hidden Number Vault

Implement iterative binary search and compare it with linear search.

## Requirement

Binary search requires sorted input.

## Linear Search

Checks elements one by one.

- Time: O(N)
- Space: O(1)

## Binary Search

Checks the middle element and discards half the search space after each
comparison.

- Time: O(log N)
- Space: O(1) for iterative implementation

## Example

Target 42 is found at index 7.

The search space shrinks:

```text
11 elements -> 5 -> 2 -> 1
```

## Interview Explanation

"Binary search works on sorted data. I maintain left and right
boundaries, inspect the middle, and discard half of the search space
based on the comparison. This gives O(log N) time and O(1) space."
