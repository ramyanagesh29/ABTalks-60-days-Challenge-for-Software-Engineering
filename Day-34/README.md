# Day 34 - The Energy Drink Analyzer

Find the maximum average of a fixed-size contiguous window.

## Naive
Recalculate every window sum: O(N*K) time, O(1) space.

## Sliding Window
Calculate the first sum once, then remove the outgoing value and add the incoming value: O(N) time, O(1) space.

For `[1,12,-5,-6,50,3]`, K=4, the answer is 12.75.

### Interview
Maintain one running window sum. Each movement does one subtraction and one addition, avoiding repeated work.
