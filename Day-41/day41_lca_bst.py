class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    current = root

    while current is not None:
        if p < current.data and q < current.data:
            current = current.left
        elif p > current.data and q > current.data:
            current = current.right
        else:
            return current

    return None


root = Node(6)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(0)
root.left.right = Node(4)
root.left.right.left = Node(3)
root.left.right.right = Node(5)
root.right.left = Node(7)
root.right.right = Node(9)

print("----- Family Reunion Locator -----")

p, q = 2, 8
ancestor = lowest_common_ancestor(root, p, q)
print("Person 1:", p)
print("Person 2:", q)
print("Lowest Common Ancestor:", ancestor.data)

p, q = 2, 5
ancestor = lowest_common_ancestor(root, p, q)
print("\nPerson 1:", p)
print("Person 2:", q)
print("Lowest Common Ancestor:", ancestor.data)

print("\nComplexity:")
print("Time: O(H)")
print("Space: O(1)")
