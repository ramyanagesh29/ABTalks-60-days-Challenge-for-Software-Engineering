# Day 41 - The Family Reunion Locator

## Objective
Find the Lowest Common Ancestor of two nodes in a Binary Search Tree.

## Strategy
Start at the root.

- If both targets are smaller, move left.
- If both targets are larger, move right.
- Otherwise the current node is the LCA.

If one target equals the current node, the current node is also the LCA.

## Example
For `p = 2` and `q = 8`, the paths split at `6`, so LCA = `6`.

For `p = 2` and `q = 5`, both are in the left subtree and the LCA is `2`.

## Complexity
- Time: O(H)
- Extra Space: O(1)

H is the height of the BST.

## Interview Explanation
"Because this is a BST, I compare both target values with the current
node. If both are smaller I go left; if both are larger I go right.
Otherwise the current node is where their paths split, so it is the
Lowest Common Ancestor."
