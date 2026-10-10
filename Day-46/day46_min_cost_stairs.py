from functools import lru_cache

def min_cost_recursive(cost):
    n = len(cost)
    def solve(i):
        if i >= n:
            return 0
        return cost[i] + min(solve(i + 1), solve(i + 2))
    return min(solve(0), solve(1))

def min_cost_memoized(cost):
    n = len(cost)
    @lru_cache(maxsize=None)
    def solve(i):
        if i >= n:
            return 0
        return cost[i] + min(solve(i + 1), solve(i + 2))
    return min(solve(0), solve(1))

def min_cost_optimized(cost):
    # dp[i] is minimum cost to reach position i; the top is position len(cost).
    previous_two = 0
    previous_one = 0
    for i in range(2, len(cost) + 1):
        current = min(previous_one + cost[i - 1],
                      previous_two + cost[i - 2])
        previous_two, previous_one = previous_one, current
    return previous_one

if __name__ == "__main__":
    cost = [10, 15, 20]
    print("Robot Energy Saver")
    print("Cost array:", cost)
    print("Recursive answer:", min_cost_recursive(cost))
    print("Memoized DP answer:", min_cost_memoized(cost))
    print("Optimized DP answer:", min_cost_optimized(cost))
