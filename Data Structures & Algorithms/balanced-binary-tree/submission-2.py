# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        is_balanced = True

        def height(node) -> int:
            nonlocal is_balanced

            if node.left:
                left = height(node.left) + 1
            else:
                left = 0
            
            if node.right:
                right = height(node.right) + 1
            else:
                right = 0
            
            if abs(left - right) > 1:
                is_balanced = False

            return max(left, right)
        
        height(root)    
        return is_balanced

        # T = O(N), N = # node in tree
        # S = O(h), h = depth of tree, recursive call stack allocation
        