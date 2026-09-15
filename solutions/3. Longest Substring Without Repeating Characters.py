class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ''
        for i in range(len(s)):
            longest = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in longest:
                    longest += s[j]
                else:
                    break
            if len(result) < len(longest):
                result = longest
        return len(result)
        