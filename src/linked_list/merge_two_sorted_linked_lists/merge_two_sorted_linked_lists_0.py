# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        c1 = list1
        c2 = list2

        if c1.val < c2.val:
            head = c1
            c1 = c1.next
        else:
            head = c2
            c2 = c2.next

        c = head

        while c1 and c2:
            if c1.val < c2.val:
                c.next = c1
                c1 = c1.next
            else:
                c.next = c2
                c2 = c2.next
            c = c.next

        c.next = c2 if not c1 else c1

        return head

        # T = O(n)
        # S = O(1)