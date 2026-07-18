# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr = l1
        l2_curr = l2
        carry = False

        while l1_curr and l2_curr:
            l1_val = l1_curr.val
            l2_val = l2_curr.val
            summ = l1_val + l2_val
            print(f'l1: {l1_val}, l2: {l2_val}')
            if carry: summ += 1
            print(f'carry: {carry}')
            print(f'pre_sum: {summ}')
            carry = False
            if summ > 9:
                carry = True
                summ -= 10
            print(f'post_sum: {summ}')
            l2_curr.val = summ

            l1_prev = l1_curr
            l2_prev = l2_curr

            l1_curr = l1_curr.next
            l2_curr = l2_curr.next
    
        if not l1_curr and not l2_curr:
            if carry:
                l2_prev.next = ListNode(val=1)     
        elif l1_curr:
            l2_prev.next = l1_curr
            while carry:
                carry = False
                if l1_curr:
                    l1_curr.val += 1
                    if l1_curr.val > 9:
                        carry = True
                        l1_curr.val -= 10
                        l1_prev = l1_curr
                        l1_curr = l1_curr.next
                else:
                    l1_prev.next = ListNode(val=1)    
        else:
            while carry:
                carry = False
                if l2_curr:
                    l2_curr.val += 1
                    if l2_curr.val > 9:
                        carry = True
                        l2_curr.val -= 10
                        l2_prev = l2_curr
                        l2_curr = l2_curr.next
                else:
                    l2_prev.next = ListNode(val=1) 
        
        return l2

        # T = O(n + m)
        # S = O(1)