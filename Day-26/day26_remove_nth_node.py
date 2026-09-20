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
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = dummy
    slow = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next


print("----- Secret Message Decoder -----")

messages = LinkedList()
for message in ["A", "B", "C", "D", "E"]:
    messages.append(message)

print("\nOriginal message chain:")
messages.display()

n = 2
messages.head = remove_nth_from_end(messages.head, n)

print("After removing the 2nd message from the end:")
messages.display()

messages2 = LinkedList()
for message in ["HELLO", "FROM", "RAMYA"]:
    messages2.append(message)

print("\nOriginal second chain:")
messages2.display()

n = 3
messages2.head = remove_nth_from_end(messages2.head, n)

print("After removing the 3rd message from the end:")
messages2.display()
