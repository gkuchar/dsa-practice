# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        curr_max = -101
        def dfs(node):
            nonlocal good
            nonlocal curr_max

            if node.val >= curr_max:
                good += 1
                curr_max = node.val

            t = curr_max

            if node.left:
                dfs(node.left)
            
            curr_max = t

            if node.right:
                dfs(node.right)

        dfs(root)
        return good

        # T = O(n), n = # nodes in tree
        # S = O(h), h = height of tree, space allocated on call stack from recursion