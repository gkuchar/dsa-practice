# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def find_half(node, p, q):
            if p.val == node.val or q.val == node.val: return node

            pval = p.val
            qval = q.val

            if (node.val < p.val and node.val > q.val) or (node.val > p.val and node.val < q.val):
                return node
            
            if node.val < p.val:
                return find_half(node.right, p, q)
            else:
                return find_half(node.left, p, q)
        
        return find_half(root, p, q)

        # T = O(lgn), n = # nodes in tree
        # S = O(h), h = height of tree, space is allocated on call stack from recursion