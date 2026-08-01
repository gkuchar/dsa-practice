# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node, vals) -> List[int]:
            if node.left:
                vals = inorder(node.left, vals)

            vals.append(node.val)

            if node.right:
                vals = inorder(node.right, vals)

            return vals
        
        sorted_vals = inorder(root, [])

        return sorted_vals[k - 1]

    # T = O(n), n = # nodes in BST
    # S = O(n)