from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = [False] * n
        adjacency_list = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if edges[i][j] == 1:
                    adjacency_list[i].append(j)
                    adjacency_list[j].append(i)

        def dfs(node):
            visited[node] = True
            for neighbour in adjacency_list[node]:
                if not visited[neighbour]:
                    dfs(neighbour)

        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        return count


solution = Solution()
n = 3
edges = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution.countComponents(n, edges))
# Time Complexity O(n^2)
