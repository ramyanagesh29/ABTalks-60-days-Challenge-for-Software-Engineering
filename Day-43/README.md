# Day 43 - The Zombie City Escape Map

## Problem
Find the shortest path from the top-left to the bottom-right of a binary
matrix using Breadth-First Search (BFS).

- `0` = open cell
- `1` = blocked cell
- Movement is allowed in 8 directions.
- Every move has equal cost.

## Algorithm
1. Put the starting cell into a queue.
2. Mark it visited.
3. Remove cells from the front of the queue.
4. Check all 8 neighboring cells.
5. Add each valid, unvisited neighbor to the queue.
6. Store its parent and distance.
7. When the destination is reached, reconstruct the path.

## Why BFS?
BFS explores level by level. Because every move has the same cost, the first
time BFS reaches the destination, the path is guaranteed to be shortest.

## Result
Shortest path length: **6**

Path:
`(0,0) -> (1,0) -> (2,1) -> (2,2) -> (3,2) -> (4,3) -> (4,4)`

## Complexity
- Time: **O(R × C)**
- Space: **O(R × C)**

## Interview Explanation
"I used BFS because this is an unweighted shortest-path problem. BFS explores
the grid level by level, so the first time I reach the destination I have found
the shortest path. I used a queue for traversal and a visited set to avoid
processing the same cell multiple times."

## Run
`python day43_zombie_city_escape.py`
