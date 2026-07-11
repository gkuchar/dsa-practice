# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        curr = head
        last = None

        while curr:
            old_next = curr.next
            curr.next = last
            last = curr
            curr = old_next
        
        return last

        # T = O(n)
        # S = O(1)