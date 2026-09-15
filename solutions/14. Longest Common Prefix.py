class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = strs[0]
        for curr in strs[1:]:
            if curr == '':
                return ''
            ind = 0
            while curr[:ind] == common[:ind] and ind <= len(common):
                ind += 1
            common = curr[:ind-1]
        return common

test = ["flower","flower","flower","flower"]
print(Solution().longestCommonPrefix(test))