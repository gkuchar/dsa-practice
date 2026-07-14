# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        new_curr = head
        last = head
        curr = head

        n = 1
        i = 0

        # get size
        while last.next:
            last = last.next
            n += 1
        
        last = head

        # traverse to mid
        while i < (n // 2) - 1:
            last = last.next
            i += 1
        
        # split into 2 distinct halves
        h2_start = last.next
        last.next = None

        # reverse second half of list
        prev = None
        curr_node = h2_start
        while curr_node:
            old_next = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = old_next
        
        # build list by altering left side and right side node
        curr = head
        tail = None
        while curr and prev:
            old_curr_next = new_curr.next
            old_prev_next = prev.next
            tail = prev

            curr.next = prev
            curr.next.next = old_curr_next
            curr = curr.next.next

            prev = old_prev_next
            new_curr = old_curr_next
        
        if n > 1 and n % 2 == 1:
            tail.next = h2_start
        
