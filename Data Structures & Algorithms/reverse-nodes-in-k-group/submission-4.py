# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head

        # split into sublists of size k
        lists = []
        curr = head
        s = 1
        short_tail = False
        while curr:
            if s % k == 1:
                new_head = curr
                curr = curr.next
            elif s % k == 0:
                next_node = curr.next
                curr.next = None
                lists.append(new_head)
                curr = next_node
            else:
                curr = curr.next
            s += 1
        
        if (s - 1) % k != 0: # explicit append final sublist if its size < k
            lists.append(new_head)
            short_tail = True
        
        # reverse each sublist, connect i - 1 head node to i tail node
        n = len(lists)
        for i, ll in enumerate(lists):
            if i == n - 1 and short_tail: # no reversal on final sublist with len < k
                lists[i - 1].next = ll
                continue

            prev = None
            curr = ll
            while curr:
                if curr.next is None: # head of combined list is tail of sublist 0
                    if i == 0:
                        head = curr 
                    else:
                        lists[i - 1].next = curr # old head of previous sublist connects to tail of current sublist
                old_next = curr.next
                curr.next = prev
                prev = curr
                curr = old_next
            
        return head

        # T = O(N)
        # S = O(N/k)
        