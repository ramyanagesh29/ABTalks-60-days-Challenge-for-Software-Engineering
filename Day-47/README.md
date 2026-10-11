# Day 47 — The Treasure Dungeon Collector

## Problem
Each room contains treasure, but adjacent rooms cannot both be selected.
Find the maximum possible total. This is the House Robber problem.

## DP state and transition
Let `dp[i]` be the maximum treasure obtainable from the first `i` rooms.
For each room, either take it or skip it:

`dp[i] = max(dp[i - 1], treasure[i - 1] + dp[i - 2])`

Base cases: `dp[0] = 0`; for a non-empty list, `dp[1] = treasure[0]`.

## Why not greedy?
A room with the largest individual treasure may prevent a better combination.
For `[2, 7, 9, 3, 1]`, choosing rooms 0, 2, and 4 gives `2 + 9 + 1 = 12`.

## Example
Maximum treasure: **12**
One optimal selection: indices `[0, 2, 4]`, treasures `[2, 9, 1]`.

## Complexity
- Memoized DP: **O(N)** time and **O(N)** space.
- Optimized bottom-up DP: **O(N)** time and **O(1)** extra space.

## Run
`python day47_treasure_dungeon.py`
