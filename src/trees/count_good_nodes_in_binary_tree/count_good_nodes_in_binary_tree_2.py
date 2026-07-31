# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(node, curr_max):
            nonlocal good

            if node.val >= curr_max:
                good += 1
                curr_max = node.val

            if node.left:
                dfs(node.left, curr_max)

            if node.right:
                dfs(node.right, curr_max)

        dfs(root, -101)
        return good

        # T = O(n), n = # nodes in tree
        # S = O(h), h = height of tree, space allocated on call stack from recursion