# Day 46 — The Robot Energy Saver

Find the minimum cost to reach the top of a staircase. You may start on step 0 or 1,
and each move climbs one or two steps. The top itself has no cost.

DP state: `dp[i]` = minimum cost to reach position `i`.
Transition: `dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])`.
Base: `dp[0] = dp[1] = 0`.

- Plain recursion: exponential time in the worst case.
- Memoization: O(N) time and O(N) space.
- Optimized bottom-up DP: O(N) time and O(1) extra space.

For `[10, 15, 20]`, the answer is **15**.
Run: `python day46_min_cost_stairs.py`
