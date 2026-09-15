class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        longest = 0
        for i in range(n):
            curr = i
            lib = {}
            exist = []
            max_freq = 0
            while curr < n:
                if s[curr] not in lib:
                    lib[s[curr]] = 1
                    exist.append(s[curr])
                else:
                    lib[s[curr]] += 1
                for cha in exist:
                    max_freq = max(max_freq, lib[cha])
                if curr-i-max_freq+1 > k:
                    break
                longest = max(longest, curr-i+1)
                curr += 1
        return longest