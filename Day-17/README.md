# Day 17 - Treasure Chest Combination Generator

## Problem

Given a list of gems, generate all possible combinations (subsets).

## Approach

I used backtracking to generate all subsets.

For every gem, there are two choices:

1. Do not take the gem
2. Take the gem

The algorithm recursively explores both choices.

## Backtracking

The main backtracking pattern is:

1. Make a choice
2. Recursively explore the choice
3. Undo the choice
4. Try the next choice

The `current` list stores the combination currently being built.

`append()` adds a selected gem and `pop()` removes it when backtracking.

## Base Case

When the index reaches the length of the gems list, all gems have been considered.

The current combination is then copied into the result list.

## Recursion Tree

Each gem creates two branches:

Take the gem
Don't take the gem

Therefore, N gems produce 2^N possible combinations.

## Example

For:

["Ruby", "Diamond", "Emerald"]

There are:

2^3 = 8

possible combinations.

## Complexity

Time Complexity: O(N × 2^N)

Space Complexity: O(N × 2^N) for storing all subsets.

The recursion stack uses O(N) space.

## Real-World Applications

Backtracking is used in:

- Scheduling systems
- Recommendation engines
- AI decision trees
- Pathfinding
- Puzzle solving
- Game decision systems

## Key Learning

I learned how backtracking explores a search space by making a choice, recursively exploring it, and then undoing the choice.

The important pattern is:

Choose → Explore → Undo → Try another choice.
