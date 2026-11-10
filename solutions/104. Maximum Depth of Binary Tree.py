# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def recurse(head, depth = 0):
            if head == None:
                return depth
            return max(recurse(head.left, depth+1), recurse(head.right, depth+1))
        return recurse(root)