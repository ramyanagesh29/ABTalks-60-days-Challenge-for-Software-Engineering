# Day 30 - The Hacker Tournament Finals

Two medium algorithm battles were solved with optimization in mind.

## Battle 1 - Longest Substring Without Repeating Characters

Uses a sliding window and hash map storing the latest index of each
character.

- Time: O(N)
- Space: O(N)

## Battle 2 - Product of Array Except Self

Uses prefix products from the left and suffix products from the right.
It does not use division.

- Time: O(N)
- Output space: O(N)
- Extra working space: O(1), excluding output

## Optimization Decisions

1. Sliding window avoids repeated substring work.
2. Hashing gives average O(1) character lookup.
3. Prefix and suffix products avoid nested loops.
4. Both solutions scale linearly with input size.

## Interview Explanation

"Good optimization removes repeated work. I use a sliding window and
hash map for the first problem, and prefix/suffix products for the
second. Both achieve O(N) time."
