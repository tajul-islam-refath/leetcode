from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)  # row size
        m = len(maze[0])  # col size
        visited = set()  # store visited cell
        queue = deque([(entrance[0], entrance[1], 0)])  # add entrance and step
        visited.add((entrance[0], entrance[1]))  # add entrance as visited
        step = float('inf')

        def valid(row, col):
            if row >= 0 and row < n and col >= 0 and col < m:
                return maze[row][col] != '+'
            else:
                return False

        def isExit(row, col):
            if row == 0 or row == n - 1 or col == 0 or col == m - 1:
                return True
            else:
                return False

        while queue:
            u = queue.popleft()

            if isExit(u[0], u[1]) and [u[0], u[1]] != entrance:
                step = min(step, u[2])

            # check right
            if valid(u[0], u[1] + 1) and (u[0], u[1] + 1) not in visited:
                queue.append((u[0], u[1] + 1, u[2] + 1))
                visited.add((u[0], u[1] + 1))
            # check left
            if valid(u[0], u[1] - 1) and (u[0], u[1] - 1) not in visited:
                queue.append((u[0], u[1] - 1, u[2] + 1))
                visited.add((u[0], u[1] - 1))
            # check bottom
            if valid(u[0] + 1, u[1]) and (u[0] + 1, u[1]) not in visited:
                queue.append((u[0] + 1, u[1], u[2] + 1))
                visited.add((u[0] + 1, u[1]))
            # check top
            if valid(u[0] - 1, u[1]) and (u[0] - 1, u[1]) not in visited:
                queue.append((u[0] - 1, u[1], u[2] + 1))
                visited.add((u[0] - 1, u[1]))

        return step if step != float('inf') else -1

