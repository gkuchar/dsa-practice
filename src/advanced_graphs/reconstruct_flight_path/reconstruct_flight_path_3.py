class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        out = {}
        ordering = []
        edge_count = {}
        curr_adj_idx = {}

        for edge in tickets:
            u = edge[0]
            v = edge[1]

            if u not in graph:
                graph[u] = []
                out[u] = 0
                curr_adj_idx[u] = 0
            
            if v not in out:
                graph[v] = []
                out[v] = 0
                curr_adj_idx[v] = 0

            if (u, v) not in edge_count:
                edge_count[(u, v)] = 0
            
            graph[u].append(v)
            out[u] += 1
            edge_count[(u, v)] += 1
        
        for node in graph:
            graph[node] = sorted(graph[node])
             
        def euler_path(node):
            for idx in range(curr_adj_idx[node], len(graph[node])):
                adj = graph[node][idx]
                if out[node] != 0 and edge_count[(node, adj)] != 0:
                    out[node] -= 1
                    edge_count[(node, adj)] -= 1
                    curr_adj_idx[node] += 1
                    euler_path(adj)
            
            ordering.append(node)
                    
        
        euler_path('JFK')

        return ordering[::-1]
        # T = O(ElogE)
        # S = O(V + E)
        