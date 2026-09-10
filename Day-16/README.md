# Day 16 - The Infinite Staircase Puzzle

## Problem

A robot is climbing a staircase.

The robot can climb either 1 step or 2 steps at a time.

The goal is to calculate the number of different ways the robot can reach step N.

## Recursive Solution

The recursive formula is:

ways(n) = ways(n - 1) + ways(n - 2)

Base cases:

ways(0) = 1
ways(1) = 1

The robot's last move can either be 1 step or 2 steps.

## Recursion Tree

For a step N, the function calls:

ways(n - 1)
ways(n - 2)

This creates a recursion tree.

The same values are calculated multiple times.

For example, ways(3) can be calculated more than once when solving a larger problem.

## Recursive Complexity

Time Complexity: O(2^N)

Space Complexity: O(N)

The recursive solution becomes slow for larger values of N because of repeated calculations.

## Memoization

Memoization stores already calculated results in a dictionary.

Before calculating a value, we check whether it already exists in the memo dictionary.

If it exists, we reuse the stored result.

## Memoization Complexity

Time Complexity: O(N)

Space Complexity: O(N)

## Speed Comparison

The normal recursive solution performs many repeated calculations.

The memoized solution calculates each value only once and reuses previously calculated results.

Therefore, memoization scales much better for larger values of N.

## Real-World Applications

Recursion and memoization are useful in:

- AI search systems
- Pathfinding
- Game development
- Compilers
- Dynamic programming
- Optimization problems

## Key Learning

I learned how recursion breaks a problem into smaller subproblems.

I also learned that repeated recursive calculations can make an algorithm very slow.

Memoization improves performance by storing and reusing previously calculated results.
