# Day 27 - The Social Media Fraud Detector

## Objective
Detect repeated social-media activity within K distance using hashing.

## Approach
Store the last index of each activity in a dictionary. For each new
activity, check whether it was seen before and whether the index
distance is at most K. Then update its latest index.

## Example
For K = 3, `"POST:Buy now!"` occurs at positions 1 and 4.

Distance = 4 - 1 = 3, so suspicious repeated activity is detected.

## Complexity
- Time: O(N) average
- Extra Space: O(N)

## Why Hashing?
A hash map provides average O(1) lookup, avoiding repeated comparisons
between many pairs of events.

## Real-World Uses
Hashing supports duplicate detection, spam filtering, bot detection,
fraud monitoring, and security systems.

## Interview Explanation
"I store the most recent index of every activity in a hash map. When the
same activity appears, I calculate the distance from its last occurrence.
If that distance is at most K, I detect the repeated activity."
