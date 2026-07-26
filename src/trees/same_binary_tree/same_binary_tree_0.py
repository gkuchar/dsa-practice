# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True

        if (not p and q) or (p and not q): return False

        def parallel_bfs(root1, root2) -> bool:
            q1 = deque([root1])
            q2 = deque([root2])

            while q1 and q2:
                node1 = q1.popleft()
                node2 = q2.popleft()

                if node1 is None and node2 is None:
                    continue
                
                if (not node1 and node2) or (node1 and not node2): return False

                if node1.val != node2.val: return False

                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)

            return True
        
        return parallel_bfs(p, q)
        
        # T = O(min(N, M)), N = # nodes in p, M = # nodes in q
        # S = O(W), W = max width of p or q