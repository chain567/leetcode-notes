# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def helper(lst):
            mid = len(lst) // 2
            node = TreeNode(lst[mid])
            left = lst[:mid]
            right = lst[mid + 1:]

            if len(left) == 1:
                node.left = TreeNode(left[0])
            elif len(left) == 0:
                node.left = None
            else:
                node.left = helper(left)
            if len(right) == 1:
                node.right = TreeNode(right[0])
            elif len(right) == 0:
                node.right = None
            else:
                node.right = helper(right)
            return node
        return helper(nums)

'''
nums = [-1,0,1,2]
n1 = Solution().sortedArrayToBST(nums)
print(n1.val)
print(n1.left.val if n1.left else None)
print(n1.right.val if n1.right else None)
'''
