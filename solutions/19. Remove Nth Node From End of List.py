# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr = head
        num = 0
        lib = {
            0: curr
        }
        while curr.next is not None:
            num += 1
            lib[num] = curr
            curr = curr.next
        if num < 1:
            return None
        elif n - num == 1:
            return head.next
        lib[num-n+1].next = lib[num-n+1].next.next
        return head