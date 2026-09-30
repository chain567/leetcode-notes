class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r,l = 0, 0
        ans = 0
        seen = set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                ans = max(ans, r-l+1)
                r += 1
            else:
                seen.remove(s[l])
                l += 1
        return ans