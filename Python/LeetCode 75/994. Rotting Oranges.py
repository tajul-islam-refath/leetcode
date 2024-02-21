from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(i, j, 0) for i in range(m) for j in range(n) if grid[i][j] == 2])
        minutes = 0

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            u = queue.popleft()
            for direction in directions:
                new_row, new_col = u[0] + direction[0], u[1] + direction[1]
                if valid(new_row, new_col):
                    queue.append((new_row, new_col, u[2] + 1))
                    grid[new_row][new_col] = 2
                    minutes = u[2] + 1

        return minutes if all(grid[i][j] != 1 for i in range(m) for j in range(n)) else -1