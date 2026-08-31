class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        valid_nodes = set()

        def dfs_cycle_detect(node, visited):
            if node in valid_nodes:
                return True

            for adj in graph[node]:
                if adj in visited:
                    return False
                
                visited.add(adj)
                is_valid = dfs_cycle_detect(adj, visited)
                if not is_valid:
                    return False
                else:
                    visited.remove(adj)
                    valid_nodes.add(adj)
            
            return True

        for node in graph:
            if not dfs_cycle_detect(node, visited=set([node])):
                return False

            valid_nodes.add(node)
        
        return True
