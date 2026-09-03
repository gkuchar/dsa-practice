from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        components = 0
        visited = set()

        def bfs(node):
            q = deque([node])

            while q:
                curr = q.popleft()
                for adj in graph[curr]:
                    if adj not in visited:
                        q.append(adj)
                        visited.add(adj)

        for node in graph:
            if node not in visited:
                visited.add(node)
                components += 1
                bfs(node)
        
        return components
        