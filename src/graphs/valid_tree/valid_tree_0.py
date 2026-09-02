class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        is_connected = False
        graph = {i : [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, path, visited, prev) -> bool:
            nonlocal is_connected

            for adj in graph[node]:
                if adj in path and adj is not prev:
                    return True
                if adj not in visited:
                    path.add(adj)
                    visited.add(adj)
                    dfs(adj, path, visited, node)
                    path.remove(adj)
            
            if len(visited) == n:
                is_connected = True

        for node in graph:
            has_cycle = dfs(node, path=set([node]), visited=set([node]), prev=None)
            if has_cycle: return False
        
        return is_connected