# Day 38 - The Ancient Kingdom Family Tree

Build a binary tree and perform inorder traversal recursively and iteratively.

Inorder order: LEFT -> ROOT -> RIGHT.

The sample tree produces: Princess C -> Prince A -> Princess D -> King -> Prince E -> Prince B -> Princess F.

Both approaches take O(N) time. Recursive space is O(H) call stack; iterative space is O(H) explicit stack.

### Interview
The iterative stack simulates the recursive call stack: keep going left, process the popped node, then move right.
