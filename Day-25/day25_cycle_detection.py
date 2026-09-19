class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return new_node

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        return new_node


def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


# Maze 1: No cycle
maze1 = LinkedList()
for value in [1, 2, 3, 4, 5]:
    maze1.append(value)

# Maze 2: Cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 3 ...
maze2 = LinkedList()
nodes = []

for value in [1, 2, 3, 4, 5]:
    nodes.append(maze2.append(value))

nodes[-1].next = nodes[2]  # 5 points back to 3

print("----- Infinite Maze Trap: Cycle Detection -----")

print("\nMaze 1: No Cycle")
print("Path: 1 -> 2 -> 3 -> 4 -> 5 -> None")
print("Cycle detected:", has_cycle(maze1.head))

print("\nMaze 2: Cycle")
print("Path: 1 -> 2 -> 3 -> 4 -> 5 -> 3 -> ...")
print("Cycle detected:", has_cycle(maze2.head))
