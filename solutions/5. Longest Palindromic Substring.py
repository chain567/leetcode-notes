class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        max_len = 0
        for i in range(len(s)):
            same_ind = 1
            while i < len(s)-1 and s[i] == s[i+1]:
                same_ind += 1
                i += 1
            left, right = i-same_ind+1, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_len = right-left
                left -= 1
                right += 1
            if curr_len > max_len:
                start = left + 1
                max_len = curr_len
        return s[start:start+max_len+1]