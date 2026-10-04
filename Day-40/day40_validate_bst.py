class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_valid_bst(root, lower=float("-inf"), upper=float("inf")):
    if root is None:
        return True

    if root.data <= lower or root.data >= upper:
        return False

    return (is_valid_bst(root.left, lower, root.data)
            and is_valid_bst(root.right, root.data, upper))


def build_valid_bst():
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    return root


def build_invalid_bst():
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(9)
    return root


def build_duplicate_bst():
    root = Node(8)
    root.left = Node(3)
    root.right = Node(8)
    return root


print("----- Corrupted Kingdom Records -----")
print("\nTest 1 - Valid BST:")
print("Result:", is_valid_bst(build_valid_bst()))

print("\nTest 2 - Invalid BST:")
print("Result:", is_valid_bst(build_invalid_bst()))

print("\nTest 3 - Duplicate Value:")
print("Result:", is_valid_bst(build_duplicate_bst()))

print("\nComplexity:")
print("Time: O(N)")
print("Space: O(H) recursion stack")
