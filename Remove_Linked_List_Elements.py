# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
       class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
         
        while head:
            if head.val == val:
                head = head.next
            else:
                break
                
        if not head:
            return head
        
        pre = head
        curr = head.next
            
        while curr:
            if curr.val == val:
                pre.next = curr.next
                curr = curr.next
            else:
                pre = curr
                curr = curr.next
        return head



        if not head:
            return head
        pre = None
        curr = head
        
        while curr:
            if curr.val == val:
                if pre:
                    pre.next = curr.next
                    curr = curr.next
                else:
                    curr = curr.next
                    head = curr
            else:
                pre, curr = curr, curr.next
         
        return head