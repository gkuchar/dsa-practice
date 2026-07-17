"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        # maintain original nodes to their idx and copy idxs to their nodes
        og_node_to_idx = {}
        copy_idx_to_node = {}

        # traverse og to build og node to idx map and copy idx to node map
        # concurrently build deep copy, setting next (but not random) pointers
        i = 0
        prev_copy = None
        curr = head
        while curr:
            og_node_to_idx[curr] = i
            copy_curr = Node(curr.val)
            copy_idx_to_node[i] = copy_curr
            if prev_copy:
                prev_copy.next = copy_curr
            else:
                new_head = copy_curr
            prev_copy = copy_curr
            curr = curr.next
            i += 1
        prev_copy.next = None

        # traverse both lists: use the maps to get the random node's idx and then set 
        # the copy's random pointer to the random node at that idx
        new_curr = new_head
        curr = head
        while new_curr:
            if curr.random:
                rand_idx = og_node_to_idx[curr.random]
                new_curr.random = copy_idx_to_node[rand_idx]
            else:
                new_curr.random = None
            new_curr = new_curr.next
            curr = curr.next

        return new_head

        # T = O(n)
        # S = O(n)
        