# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None

        # Get min val of all non empty lists, point curr to min val node
        dummy = ListNode()
        curr = dummy
        while True:
            min_i = None
            for i, ll in enumerate(lists):
                if not ll:
                    continue

                if min_i is None or ll.val < lists[min_i].val:
                    min_i = i

            if min_i is None:
                break;

            curr.next = lists[min_i]
            curr = curr.next
            lists[min_i] = lists[min_i].next
        
        return dummy.next