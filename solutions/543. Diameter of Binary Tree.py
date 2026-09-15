# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(node: TreeNode) -> int:
            nonlocal ans  # remember to use nonlocal to modify the outer variable
            if not node:
                return 0
            left, right = 0, 0
            if node.left:
                left = helper(node.left) + 1
            if node.right:
                right = helper(node.right) + 1
            highest = max(left, right)
            ans = max(ans, left+right)
            return highest
        helper(root)
        return ans