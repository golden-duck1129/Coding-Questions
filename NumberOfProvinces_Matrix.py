from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            visited[city] = True
            for neighbour in range(n):
                if isConnected[city][neighbour] == 1 and not visited[neighbour]:
                    dfs(neighbour)

        provinces = 0
        for city in range(n):
            if not visited[city]:
                provinces += 1
                dfs(city)

        return provinces


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
solution = Solution()
print(solution.findCircleNum(isConnected))
# Time Complexity : O(n^2)
