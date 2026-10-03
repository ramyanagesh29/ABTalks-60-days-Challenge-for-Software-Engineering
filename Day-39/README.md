# Day 39 - The Dungeon Depth Scanner

## Objective
Calculate the maximum depth of a binary tree using recursive DFS.

The maximum depth is the number of nodes on the longest path from the
root to a leaf.

## Recursive Strategy

For each node:

```text
depth = 1 + max(left_depth, right_depth)
```

The base case is:

```python
if root is None:
    return 0
```

## Example

The deepest path is:

```text
Entrance
-> Level 1 Left
-> Level 2 Cave
-> Level 3 Treasure Room
```

Therefore the maximum depth is `4`.

## Edge Case

For an empty tree, the depth is `0`.

## Complexity

- Time: **O(N)** because every node is visited once.
- Space: **O(H)** because recursion uses the tree height H.

For a balanced tree H is about O(log N); for a completely skewed tree H
can be O(N).

## Interview Explanation

"I use recursive DFS. For each node, I calculate the depth of its left
and right subtrees and return one plus the larger depth. The base case
for an empty node is zero. Since every node is visited once, the time
complexity is O(N) and the recursion stack uses O(H) space."
