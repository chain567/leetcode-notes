class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr = len(s) -1 
        while not s[curr].isalpha():
            curr -= 1
        end = curr
        while s[curr].isalpha() and curr >= 0:
            curr -= 1
        start = curr
        return end-start