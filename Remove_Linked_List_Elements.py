# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        
        pre = head
        while pre:
            if pre.val == val:
                pre = pre.next
            else:
                break
                
        if not pre:
            return pre
        else:
            head = pre
            curr = pre.next
            
        while curr:
            if curr.val == val:
                pre.next = curr.next
                curr = curr.next
            else:
                pre = curr
                curr = curr.next
        return head