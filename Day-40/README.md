# Day 40 - The Corrupted Kingdom Records

## Objective
Validate whether a binary tree is a valid Binary Search Tree.

A valid BST follows:

```text
all left-subtree values < node < all right-subtree values
```

## Range-Based Validation

Each node receives a valid range:

```text
lower < node.data < upper
```

The root starts with:

```text
(-infinity, +infinity)
```

For a left child, the current node becomes the upper bound.
For a right child, the current node becomes the lower bound.

This catches violations caused by any ancestor, not only the parent.

## Example of an Invalid Tree

```text
        8
       / \
      3   10
     / \
    1   9
```

Node `9` is greater than `3`, but it is in the left subtree of `8`.
Therefore its valid range is `(3, 8)`, and the tree is invalid.

## Test Cases

1. Valid BST -> `True`
2. Invalid BST -> `False`
3. Duplicate value -> `False`

Duplicates are rejected because this implementation uses strict BST
rules.

## Complexity

- Time: **O(N)**
- Space: **O(H)** recursion stack

`N` is the number of nodes and `H` is the tree height.

## Interview Explanation

"I validate the BST using DFS with lower and upper bounds. The root
starts with an unlimited range. When I go left, I update the upper
bound to the current value. When I go right, I update the lower bound.
If any value falls outside its allowed range, the tree is invalid.
This correctly enforces constraints from all ancestors."
