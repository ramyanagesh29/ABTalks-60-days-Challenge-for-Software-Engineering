# Day 23 - Train Carriage Reversal Challenge

## Problem

A railway train is represented using a singly linked list.

Each carriage is represented as a node and contains:

- Data
- A pointer to the next carriage

The task is to reverse the train by changing the links between
the carriages.

## Original Train

Carriage 1 -> Carriage 2 -> Carriage 3 -> Carriage 4 -> None

## Reversed Train

Carriage 4 -> Carriage 3 -> Carriage 2 -> Carriage 1 -> None

## Approach

I used three main pointers:

- previous
- current
- next_node

For every node:

1. Save the next node.
2. Reverse the current node's pointer.
3. Move previous to current.
4. Move current to the saved next node.

After processing all nodes, previous becomes the new head.

## Pointer Manipulation

The important operations are:

next_node = current.next

current.next = previous

previous = current

current = next_node

Saving the next node is important because changing current.next
without saving it could lose access to the remaining nodes.

## Complexity

Time Complexity: O(N)

Space Complexity: O(1)

## Real-World Applications

Linked lists are used in:

- Memory management
- Browser history
- Music playlists
- Undo/redo systems
- Real-time applications

## Key Learning

I learned how linked-list nodes are connected using pointers and
how a linked list can be reversed in-place without creating a
new linked list.

The main reversal pattern is:

SAVE -> REVERSE -> MOVE -> MOVE
