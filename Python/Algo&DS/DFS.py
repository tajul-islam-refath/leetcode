class Graph:
    def __init__(self):
        self.graph = {}
        self.visited = set()

    def add(self, vertex, neighbor):
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append(neighbor)


    def dfs(self, start):
        self.visited.add(start)
        print(f"{start}")
        for vertex in self.graph.get(start, []):
            if vertex not in self.visited:
                self.dfs(vertex)


graph = Graph()
graph.add(1, 2)
graph.add(1, 3)
graph.add(2, 4)
graph.add(4, 3)

graph.dfs(3)