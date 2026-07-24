# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def in_order(node) -> int:

            if node.left:
                left = in_order(node.left)
            else:
                left = 0

            if node.right:
                right = in_order(node.right)
            else:
                right = 0
            
            return max(left, right) + 1
        
        return in_order(root)
    
     # T = O(n), n = # nodes in tree
     # S = O(h), h = height of the tree, space allocated on the call stack