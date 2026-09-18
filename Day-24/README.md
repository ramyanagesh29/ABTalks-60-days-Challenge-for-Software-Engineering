# Day 24 - The Kingdom Alliance Merger

## Problem

Two kingdoms maintain sorted linked lists of soldiers.

The task is to merge both sorted linked lists into one sorted linked
list while preserving duplicate values.

## Example

Kingdom 1:

1 -> 3 -> 5 -> 7

Kingdom 2:

2 -> 3 -> 4 -> 8

Merged list:

1 -> 2 -> 3 -> 3 -> 4 -> 5 -> 7 -> 8

## Approach

I used two pointers, one for each linked list.

At every step, I compare the values pointed to by the two pointers.

The smaller value is connected to the merged list.

The pointer belonging to the selected node is then moved forward.

This process continues until one linked list becomes empty.

Finally, the remaining nodes of the other linked list are attached.

## Duplicate Values

Duplicate values are preserved.

For example:

List 1: 1 -> 3 -> 5

List 2: 2 -> 3 -> 4

Result:

1 -> 2 -> 3 -> 3 -> 4 -> 5

## Dummy Node

A dummy node is used to simplify the merging process.

The dummy node provides a fixed starting point for the merged list.

The actual merged list begins at dummy.next.

## Complexity

If the first list contains N nodes and the second list contains M nodes:

Time Complexity: O(N + M)

Space Complexity: O(1)

The existing nodes are reused instead of creating a new list of nodes.

## Real-World Applications

Merging sorted data is useful in:

- Database systems
- Distributed systems
- Search engines
- External sorting
- Data integration
- Log processing

## Key Learning

I learned how two sorted linked lists can be merged efficiently using
pointer manipulation.

The main strategy is:

Compare -> Choose smaller -> Move pointer -> Repeat
