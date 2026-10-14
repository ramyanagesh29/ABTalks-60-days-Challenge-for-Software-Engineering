# Day 49 — The Ultimate Engineering Gauntlet

This package includes a graph challenge, a dynamic-programming challenge, and an optimization challenge.

## 1. Graph: unweighted shortest path
BFS uses a queue and parent pointers to find a path with the fewest edges.
- Time: O(V + E)
- Space: O(V)
- Edge cases: missing nodes, unreachable target, start equals target.
For weighted graphs, BFS is not generally sufficient; consider Dijkstra for non-negative weights.

## 2. DP: Longest Increasing Subsequence (LIS)
The `tails` array keeps the smallest possible tail for each subsequence length. Binary search updates it.
- Time: O(N log N)
- Space: O(N)
- This implementation returns the length, not the actual subsequence.

## 3. Optimization: best one-transaction stock profit
Track the minimum price so far and the best profit. Evaluate the sale before updating the minimum, ensuring buy precedes sell.
- Time: O(N)
- Extra space: O(1)
- Returns zero if no profitable transaction exists.

## Engineering communication
State the approach, explain why it fits the constraints, discuss correctness, analyze complexity, and mention edge cases and alternatives.

Run each solution:
`python graph_problem.py`
`python dp_problem.py`
`python optimization_problem.py`
