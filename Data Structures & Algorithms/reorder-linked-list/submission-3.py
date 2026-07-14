# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return

        # get size
        n = 1
        i = 0

        curr = head
        while curr:
            curr = curr.next
            n += 1

        # split into 2 halves (ensure first half is equal or longer)
        curr = head
        while i < (n // 2) - 1:
            curr = curr.next
            i += 1
        
        h2_start = curr.next
        curr.next = None

        # reverse second half
        prev = None
        curr = h2_start
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next

        # build new list by iterating and altering both halves
        h2_curr = prev
        h1_curr = head
        curr = head

        while h2_curr:
            h1_next = h1_curr.next 
            h2_next = h2_curr.next 

            curr.next = h2_curr 
            curr.next.next = h1_next 
            curr = curr.next.next

            h1_curr = h1_next
            h2_curr = h2_next
        
        # T = O(n)
        # S = O(1)