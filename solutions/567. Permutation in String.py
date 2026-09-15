class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m > n:
            return False
        target = {}
        for s in s1:
            if s not in target:
                target[s] = 1
            else:
                target[s] += 1
        curr = {}
        for i in range(0, m):
            add = s2[i]
            if add not in curr:
                curr[add] = 1
            else:
                curr[add] += 1
        for idx in range(m, n+1):
            if curr == target:
                return True
            if idx < n:
                curr_s = s2[idx]
                curr[s2[idx-m]] -= 1
                if curr[s2[idx-m]] == 0:
                    del curr[s2[idx-m]]
                if curr_s in curr:
                    curr[curr_s] += 1
                else:
                    curr[curr_s] = 1
                
        return False