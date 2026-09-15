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
        currA = headA
        libA = {currA:1}

        while currA.next:
            libA[currA.next] = 1
            currA = currA.next
        
        currB = headB
        while currB:
            if currB in libA:
                return currB
            else:
                currB = currB.next


