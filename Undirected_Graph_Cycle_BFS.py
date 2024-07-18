from typing import List
from collections import deque


class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False]*V
        for i in range(V):
            if not visited[i]:
                queue = deque([(i, -1)])
                visited[i] = True

                while queue:
                    node, parent = queue.popleft()

                    for neighbour in adj[node]:
                        if not visited[neighbour]:
                            queue.append(neighbour, node)
                        elif neighbour != parent:
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
            if obj.isCycle(V, adj):
                print("1")
            else:
                print("0")

# Time Complexity: O(N+2E), Space Complexity: O(n)
