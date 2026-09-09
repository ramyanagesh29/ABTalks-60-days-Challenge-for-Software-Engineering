# Day 15 - The Duplicate Spy Detector

## Problem

Given a list of agent IDs, detect whether duplicate IDs exist.

Two approaches were implemented:
1. Brute-force duplicate detection
2. Optimized duplicate detection using a set

## Approach 1 - Brute Force

Uses two nested loops to compare each element with the elements after it.

- Time Complexity: O(N²)
- Space Complexity: O(1)

## Approach 2 - Set

Uses a `seen` set. If an ID is already in the set, it is a duplicate; otherwise it is added.

- Time Complexity: O(N) average
- Space Complexity: O(N)

## Speed Comparison

The brute-force solution becomes very slow as the dataset grows because comparisons increase quadratically.

The set-based solution scales much better because set lookup takes O(1) average time.

For large datasets such as one million IDs, the set-based approach is the better choice.

## Real-World Applications

- Fraud prevention
- Authentication systems
- Transaction validation
- Duplicate user/account detection
- Data validation

## Key Learning

I learned how to compare a brute-force O(N²) solution with an optimized O(N) solution using Python sets.

Brute Force → less extra space but much slower

Set → more extra space but much faster
