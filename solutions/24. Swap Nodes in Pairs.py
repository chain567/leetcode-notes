# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        if curr is None:
            return curr
        elif curr.next is None:
            return curr
        next_curr = curr.next
        prev = ListNode(None)
        result = prev
        while curr.next is not None:
            prev.next = next_curr
            curr.next = next_curr.next
            next_curr.next = curr
            prev = curr
            curr = curr.next
            if curr is not None:
                next_curr = curr.next
            else:
                break
        return result.next