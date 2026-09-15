# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node: TreeNode, max_val: int):
            if not node.left and not node.right:
                if node.val >= max_val:
                    return 1
                else:
                    return 0
            else:
                if node.val >= max_val:
                    max_val = node.val
                    result = 1
                else:
                    result = 0
                if node.left:
                    result += helper(node.left, max_val)
                if node.right:
                    result += helper(node.right, max_val)
                return result

        if not root:
            return 0
        else:
            return helper(root, -float("inf"))