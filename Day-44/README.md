# Day 44 — The University Course Planner

Uses Kahn's BFS-based topological sort to determine whether all courses can be completed.

1. Build edges from prerequisite to dependent course.
2. Count incoming edges (`indegree`).
3. Queue courses with indegree zero.
4. Process each queued course and reduce its neighbors' indegrees.
5. If all courses are processed, there is no cycle; otherwise, a cycle exists.

Example prerequisites `[[1,0],[2,0],[3,1],[3,2]]` produce valid order `[0,1,2,3]`.
A cycle such as `0 -> 1 -> 2 -> 0` makes completion impossible.

**Time:** O(V + E). **Space:** O(V + E).
Run: `python day44_course_schedule.py`
