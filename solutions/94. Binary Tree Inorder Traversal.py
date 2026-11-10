# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, ans):
        if root is not None:
            self.helper(root.left, ans) # in-order, so left first
            ans.append(root.val) # then middle
            self.helper(root.right, ans) # then the right
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        self.helper(root, res)
        return res