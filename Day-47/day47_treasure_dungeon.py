def rob_memoized(treasure):
    memo = {}
    def solve(i):
        if i >= len(treasure):
            return 0
        if i not in memo:
            memo[i] = max(treasure[i] + solve(i + 2), solve(i + 1))
        return memo[i]
    return solve(0)

def rob_optimized(treasure):
    two_back = 0
    one_back = 0
    for gold in treasure:
        current = max(one_back, two_back + gold)
        two_back, one_back = one_back, current
    return one_back

def dp_trace(treasure):
    dp = [0] * (len(treasure) + 1)
    for i in range(1, len(treasure) + 1):
        take = treasure[i - 1] + (dp[i - 2] if i >= 2 else 0)
        skip = dp[i - 1]
        dp[i] = max(take, skip)
    selected = []
    i = len(treasure)
    while i > 0:
        take = treasure[i - 1] + (dp[i - 2] if i >= 2 else 0)
        if take > dp[i - 1]:
            selected.append(i - 1)
            i -= 2
        else:
            i -= 1
    return dp, list(reversed(selected))

if __name__ == "__main__":
    treasure = [2, 7, 9, 3, 1]
    print("Treasure Dungeon Collector")
    print("Room treasures:", treasure)
    print("Memoized DP maximum:", rob_memoized(treasure))
    print("Optimized DP maximum:", rob_optimized(treasure))
    dp, selected = dp_trace(treasure)
    print("DP values:", dp)
    print("Selected room indices (0-based):", selected)
    print("Selected treasure:", [treasure[i] for i in selected])
