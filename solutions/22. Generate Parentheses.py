class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def helper(left, right, ans):
            if left == 0 and right == 0:
                res.append(ans)
                return
            else:
                if left > 0:
                    helper(left-1, right, ans+"(")
                if right > left:
                    helper(left, right-1, ans+")")
        helper(n, n, "")
        return res