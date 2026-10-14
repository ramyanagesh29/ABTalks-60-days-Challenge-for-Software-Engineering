# Engineering Notes — Day 49

## Graph
BFS is appropriate because all edges have equal cost. Store parent pointers to reconstruct the path and mark nodes discovered when enqueueing them. For weighted edges, consider Dijkstra when weights are non-negative.

## Dynamic programming
The LIS `tails` method maintains the smallest tail for each achievable subsequence length. Replacing a tail can improve future extension opportunities. The list itself is not necessarily the actual LIS.

## Optimization
Track the minimum price before the current day and evaluate selling at today's price before updating the minimum. This preserves buy-before-sell order.

## Test cases
- Graph: start equals target, unreachable target, missing node.
- LIS: empty input, duplicates, decreasing input, one value.
- Stock: empty input, one price, falling prices, increasing prices.

| Challenge | Time | Extra space |
|---|---|---|
| BFS shortest path | O(V + E) | O(V) |
| LIS | O(N log N) | O(N) |
| Stock profit | O(N) | O(1) |
