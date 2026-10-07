from collections import deque

def shortest_path_binary_matrix(grid):
    if not grid or not grid[0]:
        return -1, []

    rows = len(grid)
    cols = len(grid[0])

    if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0:
        return -1, []

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    queue = deque([(0, 0)])
    visited = {(0, 0)}
    parent = {(0, 0): None}
    distance = {(0, 0): 1}

    while queue:
        row, col = queue.popleft()

        if (row, col) == (rows - 1, cols - 1):
            path = []
            current = (row, col)

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return distance[(row, col)], path

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and grid[new_row][new_col] == 0
                and (new_row, new_col) not in visited
            ):
                visited.add((new_row, new_col))
                parent[(new_row, new_col)] = (row, col)
                distance[(new_row, new_col)] = distance[(row, col)] + 1
                queue.append((new_row, new_col))

    return -1, []


grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0]
]

shortest_distance, path = shortest_path_binary_matrix(grid)

print("Zombie City Escape Map")
print("----------------------")

print("Grid:")
for row in grid:
    print(row)

print("\nShortest path length:", shortest_distance)
print("Path:", path)

if shortest_distance != -1:
    print("\nEscape route found successfully!")
else:
    print("\nNo escape route exists.")
