What is Prefix Sum?

A prefix sum stores the cumulative sum of elements up to each position.

Example:

Numbers: [3, 2, 7, 4, 1]
Prefix:  [0, 3, 5, 12, 16, 17]
Brute Force

For every query, loop through the requested range and calculate the sum again.

Time complexity:

O(N × Q)

in the worst/general comparison for repeated range queries.

Optimized Prefix Sum

Calculate cumulative sums once, then answer every range query using:

prefix[right + 1] - prefix[left]

Time complexity:

Build prefix: O(N)
Each query: O(1)
Total: O(N + Q)
Real-world use

Prefix sums are useful when systems need to answer many repeated range-sum queries, such as:

Analytics dashboards
Daily sales reports
User activity data
Log and metrics processing
