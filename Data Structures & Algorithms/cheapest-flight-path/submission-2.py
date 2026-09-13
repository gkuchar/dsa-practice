import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i : [] for i in range(n)}
        rev_graph = {i : [] for i in range(n)}

        shortest_len_to_dst = {i : 101 for i in range(n)}
        shortest_len_to_dst[dst] = 0

        cheapest_valid_flight_prices = {(i, j): 1001 for i in range(n) for j in range(-1, n)}
        cheapest_valid_flight_prices[(src, k)] = 0

        for flight in flights:
            u = flight[0]
            v = flight[1]
            w = flight[2]

            graph[u].append((v, w))
            rev_graph[v].append(u)
        
        def find_shortest_len_to_dst(dst):
            processed = set()
            heap = [(0, dst)]

            while heap:
                d, node = heapq.heappop(heap)
                if d > shortest_len_to_dst[node]:
                    continue

                for adj in rev_graph[node]:
                    if adj not in processed:
                        if d + 1 < shortest_len_to_dst[adj]:
                            shortest_len_to_dst[adj] = d + 1
                            heapq.heappush(heap, (d + 1, adj))
                
                processed.add(node)
        
        def find_cheapest_valid_flight(src):
            processed = set()
            heap = [(0, src, k)]

            while heap:
                d, node, nodes_remaining = heapq.heappop(heap)
                if d > cheapest_valid_flight_prices[(node, nodes_remaining)]:
                    continue
                
                for adj, w in graph[node]:
                    if adj not in processed and shortest_len_to_dst[adj] <= nodes_remaining:
                        if d + w < cheapest_valid_flight_prices[(adj, nodes_remaining - 1)]:
                            cheapest_valid_flight_prices[(adj, nodes_remaining - 1)] = d + w
                            heapq.heappush(heap, ((d + w), adj, nodes_remaining - 1))
                
                processed.add((node, nodes_remaining))
        
        find_shortest_len_to_dst(dst)
        find_cheapest_valid_flight(src)

        min_price = 1001
        for i in range(-1, n):
            min_price = min(cheapest_valid_flight_prices[(dst, i)], min_price)

        return min_price if min_price != 1001 else -1
        

        