class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        graph = {i : [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, visited) -> bool:
            for adj in graph[node]:
                if adj not in visited:
                    visited.add(adj)
                    is_connected = dfs(adj, visited)
                    if is_connected:
                        return True
            
            if len(visited) == n:
                return True
            
            return False
        
        return dfs(0, visited=set([0]))
        # T = O(V + E)
        # S = O(V + E)