class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lib = {}
        curr = {}
        n = len(s)
        t = len(p)
        start = 0
        result = []
        for cha in p:
            if cha not in lib:
                lib[cha] = 1
            else:
                lib[cha] += 1
        for i in range(n):
            if s[i] not in curr:
                curr[s[i]] = 1
            else:
                curr[s[i]] += 1
            if i - start + 1 > t:
                curr[s[start]] -= 1
                if curr[s[start]] == 0:
                    del curr[s[start]]
                start += 1
            if i - start + 1 == t:
                same = True
                for key, val in curr.items():
                    if key not in lib or val != lib[key]:
                        same = False
                if same:
                    result.append(start)
        return result