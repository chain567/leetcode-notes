# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first_num = l1
        second_num = l2
        add_one = 0
        result = ListNode()
        curr = result

        while first_num is not None or second_num is not None or add_one != 0:
            first = first_num.val if first_num is not None else 0
            second = second_num.val if second_num is not None else 0
            total = first + second + add_one
            add_one = total // 10
            total -= 10 * add_one
            curr.next = ListNode(total)
            first_num = first_num.next if first_num is not None else None
            second_num = second_num.next if second_num is not None else None
            curr = curr.next

        return result.next