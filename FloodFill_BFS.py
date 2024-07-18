from typing import List
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        present_colour = image[sr][sc]
        queue = deque([(sr, sc)])
        if present_colour == color:
            return image
        image[sr][sc] = color
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == present_colour:
                    image[nr][nc] = color
                    queue.append((nr, nc))
        return image
