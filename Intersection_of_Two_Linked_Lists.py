# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        heads = set()
        head = headB
        while headA or headB:
            if headA:
                if headA in heads:
                    return headA
                else:
                    heads.add(headA)
                    headA = headA.next
            if headB:
                if headB in heads:
                    return headB
                else:
                    heads.add(headB)
                    headB = headB.next
                
        return None

        if not headA:
            return None
        if not headB:
            return None
        pA = headA
        pB = headB
        lA = 0
        lB = 0
        while pA.next or pB.next:
            if  pA.next:
                pA = pA.next
                lA += 1
            if pB.next:
                pB = pB.next
                lB += 1
        if pA != pB:
            return None
        if lA > lB:
            l = lA - lB
            for i in range(l):
                headA = headA.next
        if lB > lA:
            l = lB - lA
            for i in range(l):
                headB = headB.next
        while headA and headB:
            if headA == headB:
                return headB
            headA = headA.next
            headB = headB.next
