# Day 28 - The Lost Treasure Coordinates

## Objective
Solve Two Sum using both brute force and a hash map, then compare their
algorithmic performance.

## Example
Numbers = `[2, 7, 11, 15, 3, 6]`
Target = `9`

The first valid pair is `2 + 7 = 9`, with indices `[0, 1]`.

## Brute Force
Check every possible pair.

- Time: O(N^2)
- Extra Space: O(1)

## Hash Map
For every number, calculate:

```text
complement = target - number
```

If the complement is already in the dictionary, the pair is found.

- Time: O(N) average
- Extra Space: O(N)

## Lookup Visualization
```text
number = 2 -> complement = 7 -> not found -> store 2
number = 7 -> complement = 2 -> found -> pair [0, 1]
```

## Performance
The script uses `time.perf_counter()` to measure both implementations.
Exact timings vary by machine and input size. The key algorithmic
difference is O(N^2) versus O(N) average time.

## Interview Explanation
"Brute force checks every pair, taking O(N^2) time. The optimized
solution stores previously seen numbers in a hash map. For each number,
I calculate its complement and check whether it is already stored. This
reduces average time to O(N), using O(N) extra space."
