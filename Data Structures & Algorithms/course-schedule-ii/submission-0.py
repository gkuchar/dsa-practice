class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        ordering = []
        processed = set()

        def dfs_cycle(node, path):
            for adj in graph[node]:
                if adj in processed: continue

                if adj in path:
                    return True
                path.add(adj)
                cycle_found = dfs_cycle(adj, path)
                if cycle_found:
                    return True
                path.remove(adj)
            
            if node not in processed:
                ordering.append(node)
                processed.add(node)
            
            return False

        for node in graph:
            if node in processed: continue
            if dfs_cycle(node, path=set([node])): return []
        
        return ordering[::-1]
        # T = O(V + E)
        # S = O(V)
    