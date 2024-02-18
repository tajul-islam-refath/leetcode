from collections import deque


class BFS:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbor):
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append(neighbor)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            cu_vertex = queue.popleft()
            print(cu_vertex, end=" ")

            for child in self.graph.get(cu_vertex, []):
                if child not in visited:
                    queue.append(child)
                    visited.add(child)


# Example Usage:
# Create a graph
graph = BFS()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(3, 7)

# Perform BFS starting from vertex 1
print("BFS Traversal:")
graph.bfs(1)
