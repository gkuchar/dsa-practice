# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val = -1
        def inorder(node, count) -> int:
            nonlocal val
            if val >= 0: return count

            if node.left:
                count = inorder(node.left, count)

            count += 1
            if count == k:
                val = node.val
                return count

            if node.right:
                count = inorder(node.right, count)

            return count
        
        inorder(root, 0)
        return val

    # T = O(n), n = # nodes in BST
    # S = O(h), h = height BST: space allocated on call stack from recursion