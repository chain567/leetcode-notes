class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        lib = {}
        result = []
        for i in range(len(s)-9):
            curr = s[i:i+10]
            if curr in lib:
                lib[curr] += 1
                if lib[curr] == 2:
                    result.append(curr)
            else:
                lib[curr] = 1
        return result
        