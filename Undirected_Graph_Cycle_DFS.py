from typing import List


class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False] * V

        def dfs(node, parent):
            visited[node] = True
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    if dfs(neighbour, node):
                        return True
                elif neighbour != parent:
                    return True
            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True
        return False


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        V, E = map(int, input().split())
        adj = [[] for _ in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if ans:
            print("1")
        else:
            print("0")
