class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = {i : [] for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, path, visited, prev):
            for adj in graph[node]:
                if adj in path and adj is not prev:
                    print('cycle')
                    first_idx = path.index(adj)
                    print(path)
                    print(first_idx)
                    print(path[first_idx:])
                    print(set(path[first_idx:]))

                    return set(path[first_idx:])
                if adj not in visited:
                    visited.add(adj)
                    path.append(adj)
                    nodes = dfs(adj, path, visited, node)
                    if nodes:
                        return nodes
                    path.remove(adj)

        cycle_nodes = dfs(1, path=[1], visited=set([1]), prev=None)
        cycle_edges = set()

        for node in cycle_nodes:
            for v in graph[node]:
                if v in cycle_nodes and tuple(sorted((node, v))) not in cycle_edges:
                    cycle_edges.add(tuple(sorted((node, v))))
        
        print(f'cycle edges: {cycle_edges}')
        
        for i in range(n - 1, -1, -1):
            print(tuple(edges[i]))
            if tuple(edges[i]) in cycle_edges:
                return edges[i]
        