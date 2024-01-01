from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Example usage:
# Assuming the graph is represented as an adjacency list
# {node: [list of neighbors]}
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}

start_node = 1
print("BFS starting from node", start_node, ":")
bfs(graph, start_node)
