class Graph:
    def __init__(self):
        self.graph = {}
        self.visited = set()

    def add(self, vertex, neighbor):
        if vertex not in self.graph:
            self.graph[vertex] = []
        if neighbor not in self.graph:
            self.graph[neighbor] = []

        self.graph[vertex].append(neighbor)
        self.graph[neighbor].append(vertex)

    def dfs(self, start):
        self.visited.add(start)
        print(f"{start}")
        for vertex in self.graph[start]:
            if vertex not in self.visited:
                self.dfs(vertex)


graph = Graph()
graph.add(1, 2)
graph.add(1, 3)
graph.add(2, 4)
graph.add(4, 3)

graph.dfs(3)