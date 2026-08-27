"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        node_pairs = {}
        copy_start = Node(val=node.val)
        node_pairs[node] = copy_start
        bfs_q = deque([(node, copy_start)])

        while bfs_q:
            curr, copy_curr = bfs_q.popleft()
            for adj in curr.neighbors:
                if adj not in node_pairs:
                    copy_adj = Node(val=adj.val)
                    copy_curr.neighbors.append(copy_adj)
                    copy_adj.neighbors.append(copy_curr)
                    bfs_q.append((adj, copy_adj))
                    node_pairs[adj] = copy_adj
                else:
                    copy_adj = node_pairs[adj]
                    if copy_adj not in set(copy_curr.neighbors):
                        copy_curr.neighbors.append(copy_adj)
                    if copy_curr not in set(copy_adj.neighbors):
                        copy_adj.neighbors.append(copy_curr)
        
        return copy_start
                    

        