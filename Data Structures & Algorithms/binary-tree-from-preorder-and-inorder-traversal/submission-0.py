# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        val_to_in_idx = {}
        pre_idx = 0

        for i in range(n):
            for j in range(n):
                if inorder[j] == preorder[i]:
                    val_to_in_idx[preorder[i]] = j
                    break

        def build_tree(l, r):
            nonlocal pre_idx
            if l > r: return None

            root_val = preorder[pre_idx]
            pre_idx += 1
            node = TreeNode(root_val)
            in_idx = val_to_in_idx[root_val]

            node.left = build_tree(l, in_idx - 1)
            node.right = build_tree(in_idx + 1, r)

            return node
        
        return build_tree(0, n - 1)

        # T = O(n)
        # S = O(n)