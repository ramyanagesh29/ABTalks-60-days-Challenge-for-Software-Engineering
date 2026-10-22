# Debugging — Contains Duplicate

The original loop uses `range(len(nums) + 1)`. On the final iteration it accesses `nums[len(nums)]`, which is out of range and raises `IndexError`.

The fix iterates directly over values. Tests:
- `[1, 2, 3, 2]` -> `True`
- `[1, 2, 3, 4]` -> `False`
- `[]` -> `False`

Expected time: O(n); space: O(n).
