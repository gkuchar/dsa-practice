# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# S = O(n)
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = ""

        def preorder_append(node):
            nonlocal preorder

            if not node:
                preorder = preorder + 'N,'
                return
            
            preorder = preorder + f'{str(node.val)},'
            preorder_append(node.left)
            preorder_append(node.right)

        preorder_append(root)
        n = len(preorder)
        return preorder[:n - 1]
    # T = O(n), n = # nodes in tree
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        node_vals = data.split(',')
        i = 0
        n = len(node_vals)

        def build_tree() -> Optional[TreeNode]:
            nonlocal node_vals
            nonlocal i

            if node_vals[i] == 'N':
                i += 1
                return None

            node = TreeNode(val=int(node_vals[i]))

            i += 1
            node.left = build_tree()
            node.right = build_tree()

            return node
        
        return build_tree()
     # T = O(n), n = # nodes in tree