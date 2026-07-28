# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        is_subtree = False
        def dfs(node) -> bool:
            nonlocal is_subtree
            stack = [node]
            while stack:
                curr = stack.pop()

                if curr and curr.val == subRoot.val:
                    is_subtree = parallel_dfs(curr, subRoot)
                
                if is_subtree:
                    return True

                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
            
            return False
        
        def parallel_dfs(root, sub):
            stack_root = [root]
            stack_sub = [sub]

            while stack_root and stack_sub:
                curr_root = stack_root.pop()
                curr_sub = stack_sub.pop()

                if not curr_root and not curr_sub:
                    continue
                
                if (curr_root and not curr_sub) or (not curr_root and curr_sub) or curr_root.val != curr_sub.val:
                    return False
                
                stack_root.append(curr_root.right)
                stack_sub.append(curr_sub.right)

                stack_root.append(curr_root.left)
                stack_sub.append(curr_sub.left)
            
            return True
        
        return dfs(root)