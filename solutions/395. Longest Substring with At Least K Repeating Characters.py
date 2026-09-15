class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        longest = 0
        for u in range(1, 27):
            unique = {}
            left = 0
            curr_u = 0
            for i in range(len(s)):
                curr = s[i]
                if curr not in unique:
                    unique[curr] = 1
                    curr_u += 1
                else:
                    unique[curr] += 1
                while curr_u > u:
                    unique[s[left]]-=1
                    if unique[s[left]] == 0:
                        curr_u -= 1
                        del unique[s[left]]
                    left += 1
                if curr_u == u:
                    reached = True
                    for key, val in unique.items():
                        if val > 0 and val < k:
                            reached = False
                    if reached:
                        longest = max(longest, i-left+1)
        return longest