# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def post_order(node) -> int:
            nonlocal diameter

            if node.left:
                left = post_order(node.left) + 1
            else:
                left = 0
            
            if node.right:
                right = post_order(node.right) + 1
            else:
                right = 0

            diameter = max(diameter, left + right)
            return max(left, right)

        post_order(root)
        return diameter

        # T = O(N), N = # nodes in tree
        # S = O(h), h = depth of tree, space allocated in call stack due to recursion