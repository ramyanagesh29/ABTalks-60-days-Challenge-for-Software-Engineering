# Day 36 - The Water Reservoir Architect

Compare brute force and the two-pointer solution for Container With Most Water.

Brute force checks every pair: O(N^2), O(1) space.

Two pointers start at both ends. Calculate area, then move the shorter wall. The shorter wall limits the current area; moving the taller wall cannot improve the limiting height while width decreases.

Two-pointer complexity: O(N) time, O(1) space.

### Interview
Move the smaller wall because it is the bottleneck.
