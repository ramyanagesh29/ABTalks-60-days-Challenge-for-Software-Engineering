# Day 24 - The Kingdom Alliance Merger


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


def merge_sorted_lists(head1, head2):

    # Dummy node makes merging easier
    dummy = Node(0)

    current = dummy

    while head1 is not None and head2 is not None:

        if head1.data <= head2.data:

            current.next = head1
            head1 = head1.next

        else:

            current.next = head2
            head2 = head2.next

        current = current.next

    # Attach remaining nodes
    if head1 is not None:
        current.next = head1

    else:
        current.next = head2

    return dummy.next


# Create first sorted kingdom
kingdom1 = LinkedList()

kingdom1.append(1)
kingdom1.append(3)
kingdom1.append(5)
kingdom1.append(7)


# Create second sorted kingdom
kingdom2 = LinkedList()

kingdom2.append(2)
kingdom2.append(3)
kingdom2.append(4)
kingdom2.append(8)


print("----- Kingdom Alliance Merger -----")

print("\nKingdom 1:")
kingdom1.display()

print("\nKingdom 2:")
kingdom2.display()


merged_head = merge_sorted_lists(
    kingdom1.head,
    kingdom2.head
)


print("\nMerged Master Army:")

current = merged_head

while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")
