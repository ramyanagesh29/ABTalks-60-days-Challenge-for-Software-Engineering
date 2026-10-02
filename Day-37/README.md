# Day 37 - The Cookie Distribution Crisis

Sort children and cookies, then use two pointers. Give the smallest cookie that can satisfy the smallest remaining requirement. If a cookie is too small, discard it because it cannot satisfy a child with a larger requirement.

Sorting: O(N log N + M log M). Traversal: O(N+M).

### Interview
The local choice preserves the largest possible resources for children with larger requirements.
