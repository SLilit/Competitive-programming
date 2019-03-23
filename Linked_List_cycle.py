# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head == None:
            return False
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
        

        slow = head
        fast = head.next
        try:
            while slow:
                if slow == fast:
                    return True
                slow = slow.next
                fast = fast.next.next
        except:
            return False
        return False