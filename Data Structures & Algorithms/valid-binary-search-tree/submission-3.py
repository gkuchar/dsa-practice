# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(node, lower_bound, upper_bound) -> bool:

            if not node.left:
                left = True
            else:
                left = isValid(node.left, lower_bound, node.val)

            if not node.right:
                right = True
            else:
                right = isValid(node.right, node.val, upper_bound)

            if left and right and node.val > lower_bound and node.val < upper_bound:
                return True
            else:
                return False

        return isValid(root, float('-inf'), float('inf'))

        # T = O(n), n = # nodes in Tree
        # S = O(h), h = height of tree, space allocated on call stack from recursion