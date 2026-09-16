# Day 22 - The Theme Park FastPass Simulator

## Problem

Build a theme park ride scheduling system where visitors join a normal
queue, while VIP visitors receive priority access.

The system should process visitors in the correct order.

## Queue Concept

A queue follows FIFO:

First In, First Out.

The visitor who joins first is normally processed first.

Example:

A -> B -> C

Processing order:

A -> B -> C

## VIP Priority

The simulator maintains two queues:

1. Normal queue
2. VIP queue

VIP visitors are processed before normal visitors.

However, VIP visitors maintain FIFO order among themselves.

Normal visitors also maintain FIFO order among themselves.

Example:

VIP Queue:

Anu -> Priya

Normal Queue:

Ramya -> Rahul -> Kiran

Processing order:

Anu -> Priya -> Ramya -> Rahul -> Kiran

## Queue Operations

### Enqueue

Visitors are added using:

append()

### Dequeue

The first visitor is removed using:

pop(0)

## Complexity

For the educational list implementation:

append(): O(1)

pop(0): O(N)

For a production implementation using collections.deque:

append(): O(1)

popleft(): O(1)

## Real-World Applications

Queue systems are used in:

- Ticket booking
- Customer support
- Operating systems
- Cloud task scheduling
- Print queues
- Network request processing

Priority queues or priority lanes are used when some tasks need to
be processed before others.

## Key Learning

I learned that queues follow FIFO behavior.

I also learned how priority handling can be implemented by maintaining
separate queues for different priority levels.

The main pattern is:

VIP queue first -> Normal queue second
