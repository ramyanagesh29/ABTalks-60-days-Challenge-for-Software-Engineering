from collections import deque

def shortest_path(graph, start, target):
    if start not in graph or target not in graph:
        return []
    queue = deque([start])
    parent = {start: None}
    while queue:
        node = queue.popleft()
        if node == target:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        for neighbor in graph.get(node, []):
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    return []

if __name__ == "__main__":
    graph = {"A":["B","C"], "B":["A","D","E"], "C":["A","F"],
             "D":["B"], "E":["B","F"], "F":["C","E"]}
    path = shortest_path(graph, "A", "F")
    print("Graph challenge: shortest path")
    print("Path from A to F:", path)
    print("Number of edges:", len(path)-1 if path else -1)
