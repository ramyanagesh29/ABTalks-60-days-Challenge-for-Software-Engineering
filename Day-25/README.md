# Day 25 - The Infinite Maze Trap

## Objective

Detect whether a linked-list maze contains an infinite cycle using
Floyd's Cycle Detection Algorithm, also called the Fast and Slow
Pointer technique.

## Concept

A cycle occurs when a node points back to an earlier node instead of
eventually pointing to `None`.

Example:

```text
1 -> 2 -> 3 -> 4 -> 5
          ^         |
          |_________|
```

Here, node 5 points back to node 3.

## Floyd's Cycle Detection

Two pointers are used:

- `slow` moves one node at a time.
- `fast` moves two nodes at a time.

If a cycle exists, the fast pointer will eventually catch the slow
pointer.

If `fast` reaches `None`, there is no cycle.

## Algorithm

```text
slow = head
fast = head

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        cycle exists

otherwise:
    no cycle
```

## Test Cases

### Maze 1 - No Cycle

```text
1 -> 2 -> 3 -> 4 -> 5 -> None
```

Result:

```text
Cycle detected: False
```

### Maze 2 - Cycle

```text
1 -> 2 -> 3 -> 4 -> 5
          ^         |
          |_________|
```

Node 5 points back to node 3.

Result:

```text
Cycle detected: True
```

## Complexity

- Time Complexity: **O(N)**
- Space Complexity: **O(1)**

The algorithm does not need an additional set or list to remember
visited nodes.

## Why Cycle Detection Matters

Cycle detection is useful when a system can accidentally enter an
infinite loop. Similar ideas are useful in:

- Linked lists
- Operating-system resource/dependency analysis
- Dependency graphs
- Distributed systems
- Workflow and state-machine validation

## Key Learning

The important pattern is:

**Fast pointer + Slow pointer = O(1) space cycle detection**

## Interview Explanation

Floyd's Cycle Detection works because when two pointers move at
different speeds inside a cycle, the faster pointer eventually catches
the slower pointer. If there is no cycle, the fast pointer reaches the
end of the linked list.
