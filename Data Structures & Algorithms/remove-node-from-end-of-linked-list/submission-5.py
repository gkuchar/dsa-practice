# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # get size
        sz = 0
        curr = head
        while curr:
            sz += 1
            curr = curr.next
        print(f'size = {sz}')
        
        if sz == 1: return None

        # traverse to sz - (n + 1)
        curr = head
        for i in range(sz - (n + 1)):
            curr = curr.next
        print(f'curr lands on node before the node to be removed: {curr.val}')

        # save node sz - (n + 1) and node beyond sz - n
        prev = curr
        if prev is head and sz == n: return prev.next
        beyond = curr.next.next if curr.next else None

        # sz - (n + 1).next = sz - n.next | sz - n.next = none
        prev.next = beyond
        
        return head