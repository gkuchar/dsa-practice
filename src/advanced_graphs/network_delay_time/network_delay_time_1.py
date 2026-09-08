import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {node : [] for node in range(1, n+1)}
        for edge in times:
            u = edge[0]
            v = edge[1]
            w = edge[2]

            graph[u].append((v, w))
        
        def dijkstras(graph, start):
            weights = {node : float('inf') for node in range(1, n+1)}
            weights[start] = 0
            max_weight = float('-inf')

            processed = set()
            count = 0
            heap = [(0, start)]

            while heap:
                d, node = heapq.heappop(heap)

                if d > weights[node]: continue

                for adj, w in graph[node]:
                    if adj not in processed:
                        d_through_node = weights[node] + w
                        if d_through_node < weights[adj]:
                            weights[adj] = d_through_node
                            heapq.heappush(heap, (d_through_node, adj))
                
                processed.add(node)
                max_weight = max(max_weight, weights[node])
                count += 1
            
            return max_weight, count

        
        max_weight, count = dijkstras(graph, k)
        if count != n:
            return -1
        
        return max_weight
        # T = O(logV * (V + E))
        # S = O(V + E)
