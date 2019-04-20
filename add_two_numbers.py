# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def helper(l, s):
            head = l
            l_sum = l.val + s
            if l_sum < 10:
                l.val = l_sum
            else:
                while l_sum == 10 and l.next:
                    l.val = 0
                    l = l.next
                    l_sum = l.val + s
                
                if l_sum < 10:
                    l.val = l_sum    
                else:
                    l.val = 0
                    l.next = ListNode(1)
            return head

        l_remaining = 0        
        num = head = ListNode(None)
        while l1 and l2:
            l_sum = l1.val + l2.val + l_remaining
            l1 = l1.next
            l2 = l2.next

            if l_sum < 10:
                head.next = ListNode(l_sum)
                head = head.next
                l_remaining = 0
            else:
                head.next = ListNode(l_sum % 10)
                head = head.next
                l_remaining = 1
        
        if l1:
            head.next = helper(l1, l_remaining)
        elif l2:
            head.next = helper(l2, l_remaining)
        elif l_remaining:
            head.next = ListNode(1)
        
        
            
        return num.next
                
                
                
            
                