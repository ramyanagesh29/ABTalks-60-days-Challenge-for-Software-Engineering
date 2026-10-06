def num_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    columns = len(grid[0])
    island_count = 0

    def dfs(row, column):
        if (row < 0 or row >= rows or
                column < 0 or column >= columns or
                grid[row][column] != "1"):
            return

        grid[row][column] = "0"

        dfs(row - 1, column)
        dfs(row + 1, column)
        dfs(row, column - 1)
        dfs(row, column + 1)

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == "1":
                island_count += 1
                dfs(row, column)

    return island_count


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "1", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print("----- Island Survival Simulator -----")
print("Original map:")
for row in grid:
    print(" ".join(row))

result = num_islands(grid)

print("\nNumber of separate islands:", result)

print("\nComplexity:")
print("Time: O(R * C)")
print("Space: O(R * C) worst-case DFS stack")
