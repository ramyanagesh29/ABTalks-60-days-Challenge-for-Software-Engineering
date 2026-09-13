# Day 19 - The Temperature Vault

## Problem

Build a Min Stack that stores temperature readings and can return
the minimum recorded temperature at any moment.

The stack must support:

- push()
- pop()
- get_min()

The minimum temperature must be returned in O(1) time.

## Approach

I implemented a custom Min Stack using two stacks.

### Main Stack

The main stack stores all temperature readings.

### Minimum Stack

The minimum stack stores the minimum temperature at every stack level.

Whenever a new temperature is pushed, the current minimum is calculated
and stored in the minimum stack.

When an item is removed, both stacks are popped.

The top of the minimum stack always contains the current minimum.

## Example

Temperatures:

[25, 18, 30, 12, 20]

Main stack:

[25, 18, 30, 12, 20]

Minimum stack:

[25, 18, 18, 12, 12]

Therefore, get_min() returns 12 immediately.

After removing 20:

Minimum is still 12.

After removing 12:

Minimum becomes 18.

## Complexity

push(): O(1)

pop(): O(1)

get_min(): O(1)

Space Complexity: O(N)

## Why an Auxiliary Stack?

A normal stack would require scanning all elements to find the minimum,
which would take O(N) time.

The auxiliary minimum stack keeps track of the minimum at every level,
allowing the minimum to be retrieved in O(1) time.

## Real-World Applications

This type of data structure can be useful in:

- Temperature monitoring systems
- Financial monitoring
- Cloud infrastructure
- Sensor data processing
- Real-time analytics

## Key Learning

I learned how to design a custom data structure using an auxiliary stack
to maintain additional state efficiently.

The main idea is to maintain the minimum value while performing normal
stack operations without scanning the entire stack.
