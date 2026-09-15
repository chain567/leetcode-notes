# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ind = 0
        curr = head
        lib = {
            curr: ind
        }
        curr = curr.next
        while curr is not None and curr.next:
            if curr not in lib:
                lib[curr] = ind
                curr = curr.next
                ind += 1
            else:
                return True
        return False

head = ListNode(1)
second = ListNode(2)
head.next = second
print(Solution().hasCycle(head))
