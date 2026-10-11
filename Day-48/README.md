# Day 48 — The Alien Language Translator

## Problem
Find the minimum number of single-character insertions, deletions, and
replacements needed to transform one string into another. Each edit costs 1.
This is the Edit Distance (Levenshtein distance) problem.

## DP State
`dp[i][j]` is the minimum edits needed to transform the first `i` characters
of `source` into the first `j` characters of `target`.

## Base cases
- `dp[i][0] = i`: delete all source characters.
- `dp[0][j] = j`: insert all target characters.

## Transition
If the current characters match, copy the diagonal: `dp[i][j] = dp[i-1][j-1]`.
Otherwise:
`dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])`
These represent insertion, deletion, and replacement respectively.

## Example
`horse` -> `ros` has edit distance **3**.
One sequence: `horse` -> `rorse` (replace h with r) -> `rose` (delete r)
-> `ros` (delete e).

## Complexity
- Naive recursion: exponential time due to repeated subproblems.
- Memoized DP: **O(m × n)** time and space.
- Bottom-up full table: **O(m × n)** time and space.
`m` and `n` are the lengths of the two strings.

## Run
`python day48_edit_distance.py`
