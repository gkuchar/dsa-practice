# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root

        def swap(node):
            t = node.left
            node.left = node.right
            node.right = t
        
        def post_order(node):
            if node.left:
                post_order(node.left)

            if node.right:
                post_order(node.right)

            swap(node)
        
        post_order(root)

        return root

        # T = O(n)
        # S = O(h), h = height of tree. Recursion allocates storage on call stack