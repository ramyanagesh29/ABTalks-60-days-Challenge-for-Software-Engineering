# Day 10 - Kadane's Algorithm

## Problem

The goal is to find the maximum sum of a continuous subarray.

## Approach

I used Kadane's Algorithm to solve the maximum subarray problem efficiently.

The algorithm keeps track of two values:

* `current_sum`: The maximum sum of a subarray ending at the current position.
* `max_sum`: The maximum subarray sum found so far.

For every number, the algorithm compares two choices:

1. Continue the current subarray by adding the current number.
2. Start a new subarray from the current number.

The larger value becomes the new `current_sum`.

Then `max_sum` is updated if the new `current_sum` is greater.

## Time Complexity

O(N)

The algorithm loops through the array only once.

## Space Complexity

O(1)

Only two extra variables are used.

## Real-World Usage

Kadane's Algorithm can be used in financial and analytics systems to find the best continuous period of profit or performance. For example, it can help identify the period with the maximum total profit from daily profit and loss data.

## Key Learning

Kadane's Algorithm is an optimization technique that avoids checking every possible subarray. Instead, it keeps track of the best running sum and decides whether continuing the current subarray or starting a new one gives a better result.
