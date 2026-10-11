def edit_distance_memoized(source, target):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def solve(i, j):
        if i == len(source):
            return len(target) - j
        if j == len(target):
            return len(source) - i
        if source[i] == target[j]:
            return solve(i + 1, j + 1)
        return 1 + min(
            solve(i, j + 1),      # insert
            solve(i + 1, j),      # delete
            solve(i + 1, j + 1)   # replace
        )
    return solve(0, 0)


def edit_distance_table(source, target):
    m, n = len(source), len(target)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],     # insert
                    dp[i - 1][j],     # delete
                    dp[i - 1][j - 1]  # replace
                )
    return dp[m][n], dp


def print_table(source, target, dp):
    print("      " + "  ".join(f"{c:>2}" for c in ["∅"] + list(target)))
    for i, row in enumerate(dp):
        label = "∅" if i == 0 else source[i - 1]
        print(f"{label:>3}   " + "  ".join(f"{v:>2}" for v in row))


if __name__ == "__main__":
    source, target = "horse", "ros"
    distance, dp = edit_distance_table(source, target)
    print("Alien Language Translator")
    print("Source:", repr(source))
    print("Target:", repr(target))
    print("Memoized DP answer:", edit_distance_memoized(source, target))
    print("Bottom-up DP answer:", distance)
    print("DP table (rows = source prefix, columns = target prefix):")
    print_table(source, target, dp)
