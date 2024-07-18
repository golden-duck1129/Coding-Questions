from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = 0
        queue = deque()
        fresh_oranges = 0
        minutes_passed = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        while queue:
            r, c, minutes = queue.popleft()
            minutes_passed = max(minutes_passed, minutes)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if len(grid) > nr >= 0 and len(grid[0]) > nc >= 0 and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    queue.append((nr, nc, minutes+1))

        if fresh_oranges > 0:
            return -1

        return minutes
