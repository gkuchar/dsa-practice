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
        
        if sz == 1: return None # remove the only node since n <= sz
        if sz == n: return head.next # remove the head

        # traverse to sz - (n + 1)
        curr = head
        for i in range(sz - (n + 1)):
            curr = curr.next

        # save node sz - (n + 1) and the node beyond sz - n
        prev = curr
        beyond = curr.next.next if curr.next else None

        # sz - (n + 1).next = sz - n.next | sz - n.next = none
        prev.next = beyond
        
        return head

        # T = O(N), N = len(list)
        # S = O(1)