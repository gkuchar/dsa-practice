# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder[i] indicates root of current tree
        # inorder[i] partitions preorder[i] on its left and right subtress

        n = len(preorder)
        pre_idx = 0

        # map a value to its inorder index - only possible due to uniqueness constraint
        val_to_in_idx = {}
        for i in range(n):
            val_to_in_idx[inorder[i]] = i
        
        # create root based on preorder value
        # recursively create and connect left subtree using bounds l, in_idx - 1
        # recursively create and connect right subtree using bounds in_idx + 1, r
        def build_tree(l, r):
            nonlocal pre_idx
            if l > r: return None

            node_val = preorder[pre_idx]
            pre_idx += 1
            in_idx = val_to_in_idx[node_val]

            node = TreeNode(val=node_val)
            node.left = build_tree(l, in_idx - 1)
            node.right = build_tree(in_idx + 1, r)

            return node
        
        return build_tree(0, n - 1)

        # T = O(n), populating val_to_in_idx + constant work per entry in the arrays
        # S = O(n), val_to_in_idx map