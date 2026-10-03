class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_depth(root):
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)


root = Node("Entrance")
root.left = Node("Level 1 - Left")
root.right = Node("Level 1 - Right")
root.left.left = Node("Level 2 - Cave")
root.left.right = Node("Level 2 - Hall")
root.left.left.left = Node("Level 3 - Treasure Room")
root.right.right = Node("Level 2 - Chamber")
root.right.right.right = Node("Level 3 - Exit")

print("----- Dungeon Depth Scanner -----")
print("Maximum dungeon depth:", max_depth(root))

print("\nEdge Case - Empty Dungeon:")
print("Maximum depth:", max_depth(None))

print("\nComplexity:")
print("Time: O(N)")
print("Space: O(H) recursion stack")
