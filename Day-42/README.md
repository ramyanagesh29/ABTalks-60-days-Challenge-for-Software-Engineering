# Day 42 - The Island Survival Simulator

## Objective
Count separate islands in a grid using DFS.

`1` represents land and `0` represents water. Cells connected
vertically or horizontally belong to the same island. Diagonal
connections do not count.

## DFS Strategy
Scan every cell. When an unvisited land cell is found:
1. Increase the island count.
2. Start DFS.
3. Visit connected land in four directions.
4. Mark visited land as `0`.

This prevents counting the same island again.

## Example
```text
1 1 0 0 0
1 1 0 1 0
0 0 1 0 0
0 0 0 1 1
```

There are 4 islands.

## Complexity
For R rows and C columns:
- Time: O(R * C)
- Space: O(R * C) worst case for recursive DFS stack

Every cell is processed at most once.

## Interview Explanation
"I scan the grid and start DFS whenever I find unvisited land. DFS
marks the entire connected island as visited by changing its cells to
water. Therefore each island is counted exactly once."
