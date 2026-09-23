# Day 29 - The Viral Hashtag Tracker

## Objective
Find the Top K most frequently used hashtags using frequency counting,
sorting, and a heap.

## Example
For the supplied data, frequencies are:

```text
#python -> 5
#ai     -> 4
#coding -> 3
#tech   -> 2
#cloud  -> 1
```

For K = 3, the result is `#python`, `#ai`, and `#coding`.

## Frequency Counting
A dictionary stores the number of occurrences of every hashtag.

## Approach 1 - Sorting
Sort all unique hashtags by frequency in descending order and take the
first K.

If N is the total number of hashtags and U is the number of unique
hashtags:
- Time: O(N + U log U)
- Space: O(U)

## Approach 2 - Min Heap
Maintain a min-heap of size K. Add every unique hashtag and remove the
smallest whenever the heap exceeds K.

- Time: O(N + U log K)
- Space: O(U + K)

A heap is useful when there are many unique elements but K is small.

## Real-World Applications
Top-K frequency analysis appears in trending hashtags, search
suggestions, recommendation systems, popular content ranking, and log
analysis.

## Interview Explanation
"First I count each hashtag with a hash map. Then I can sort all unique
hashtags or maintain a min-heap of size K. Sorting costs O(N + U log U),
while the heap costs O(N + U log K) average time, making the heap useful
when K is much smaller than U."
