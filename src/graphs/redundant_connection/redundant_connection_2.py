class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # intuition: the redundant connection is any edge of the cycle
        # Thus, find all cycle edges and return the one that appear last in edges

        # Build undirected graph
        n = len(edges)
        graph = {i : [] for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # DFS traversal to detect cycle and return the nodes of the cycle
        # path is key for cycle detcion, prev is needed to not declare a one edge cycle between two nodes
        def dfs(node, path_list, path, visited, prev):
            for adj in graph[node]:
                if adj in path and adj != prev:
                    # cycle runs from adj to adj, so return the nodes from the first appearance of adj to end of path
                    first_idx = path_list.index(adj)

                    return set(path_list[first_idx:])
                if adj not in visited:
                    visited.add(adj)
                    path_list.append(adj)
                    path.add(adj)
                    nodes = dfs(adj, path_list, path, visited, node)
                    if nodes:
                        return nodes
                    path_list.pop()
                    path.remove(adj)

        cycle_nodes = dfs(1, path_list=[1], path=set([1]), visited=set([1]), prev=-1)
        cycle_edges = set()

        # build cycle edges from cycle nodes: cycle edge if both nodes are in cycle_nodes
        # nodes are sorted within an edge to match edges
        # tuple is used since List cannot be hashed into a set
        for node in cycle_nodes:
            for v in graph[node]:
                if v in cycle_nodes and tuple(sorted((node, v))) not in cycle_edges:
                    cycle_edges.add(tuple(sorted((node, v))))
        
        # traverse edges in reverse order to find the latest edge in edges that appears in cycle_edges
        for i in range(n - 1, -1, -1):
            if tuple(sorted(edges[i])) in cycle_edges:
                return edges[i]
        
        # T = O(V + E)
        # S = O(V + E)