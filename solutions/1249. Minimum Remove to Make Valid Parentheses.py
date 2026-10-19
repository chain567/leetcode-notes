class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
                stack.append(c)
            elif c == ')' and cnt > 0:
                cnt -= 1
                stack.append(c)
            elif c != ')': # all alpha numerical chars other than '(' and ')'
                stack.append(c)
        ans = ""
        while stack:
            x = stack.pop()
            if x == '(' and cnt > 0:
                cnt -= 1
            else:
                ans = x + ans
        return ans
