# Two Sum — Solution Notes

Use a hash map from previously seen values to indices. For each value, calculate `target - value`. If it is already in the map, return the stored index and current index; otherwise store the current value.

- Expected time: **O(n)**
- Extra space: **O(n)**

Interview explanation: “I store values I have already visited in a hash map. For each number, I check whether its complement is already present. This avoids checking every pair and gives expected O(n) time.”
