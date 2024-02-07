class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0 for i in range(len(isConnected))]

        def dfs(start, color):
            visited[start] = color
            for j in range(len(isConnected[start])):
                if isConnected[start][j] == 1 and visited[j] == 0:
                    dfs(j, color)

        for i in range(len(visited)):
            if visited[i] == 0:
                dfs(i, i + 1)

        provinces = {i: i for i in visited}
        return len(provinces)