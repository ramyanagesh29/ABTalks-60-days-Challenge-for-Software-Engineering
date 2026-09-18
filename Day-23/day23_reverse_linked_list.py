# Day 23 - Train Carriage Reversal Challenge


# Node represents one train carriage
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List
class LinkedList:

    def __init__(self):
        self.head = None

    # Add a carriage at the end
    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Print the linked list
    def display(self):

        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # Reverse the linked list
    def reverse(self):

        previous = None
        current = self.head

        while current is not None:

            next_node = current.next

            current.next = previous

            previous = current
            current = next_node

        self.head = previous


# Create train
train = LinkedList()

train.append("Carriage 1")
train.append("Carriage 2")
train.append("Carriage 3")
train.append("Carriage 4")

print("----- Train Carriage Reversal -----")

print("\nOriginal train:")
train.display()

train.reverse()

print("\nReversed train:")
train.display()
