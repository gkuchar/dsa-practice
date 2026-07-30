# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_vals = []
        if not root: return right_vals

        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                rval = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            right_vals.append(rval)
        
        return right_vals

        # T = O(n), n = # nodes in tree
        # S = O(w), w = max width of tree