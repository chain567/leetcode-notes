class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        for t in s:
            if t.isalnum():
                res.append(t.lower())
        result = "".join(res)
        start = 0
        end = len(result)-1
        while start < end:
            if result[start] != result[end]:
                return False
            start += 1
            end -= 1
        return True