# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = root.val

        def max_path(node) -> int:
            nonlocal maximum

            if node.left:
                left = max(0, max_path(node.left))
            else:
                left = 0
            
            if node.right:
                right = max(0, max_path(node.right))
            else:
                right = 0
            
            maximum = max(maximum, left + right + node.val)

            return node.val + max(left, right)
        
        max_path(root)
        return maximum

        # T = O(n), n = # nodes in tree
        # S = O(h), h = height of tree, space allocated on call stack from recursion