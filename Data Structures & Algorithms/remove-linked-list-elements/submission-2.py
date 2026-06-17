# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                continue
            
            curr = curr.next
        
        return dummy.next

        # T = O(n)
        # S = O(1)