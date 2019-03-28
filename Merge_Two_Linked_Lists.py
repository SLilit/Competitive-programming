# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1 == l2 == None:
            return None
        
        if l1.val > l2.val:
            tmp = l2
            l2 = l2.next
        else: 
            tmp = l1
            l1 = l1.next
        head = tmp
        
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
            
        if l1:
            tmp.next = l1
        if l2:
            tmp.next = l2
        return head