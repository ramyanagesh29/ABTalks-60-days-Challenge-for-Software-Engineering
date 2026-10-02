# Day 35 - The Hacker Signal Decoder

Find the longest substring without repeating characters using a variable sliding window.

`right` expands the window, `left` moves forward after a repetition, and a dictionary stores the latest index.

Time: O(N). Space: O(N).

Example: `abcabcbb` -> `abc`, length 3.

### Interview
The window only moves forward, so each character is handled a constant number of times.
