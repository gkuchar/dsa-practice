import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        unvisited = {tuple(point) for point in points}
        cost = 0

        start = tuple(points[0])
        visited = set()
        heap = [(0, start)]

        while heap:
            d, curr = heapq.heappop(heap)

            if curr in visited:
                continue

            cost += d
            unvisited.remove(curr)

            xi = curr[0]
            yi = curr[1]

            for p in unvisited:
                xj = p[0]
                yj = p[1]

                d = abs(xi - xj) + abs(yi - yj)
                heapq.heappush(heap, (d, p))

            
            visited.add(curr)
        
        return cost
        # T = O(lgV * V^2)
        # S = O(V^2)


        