class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        dic = {'I':1, 'V': 5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)-1):
            curr = s[i]
            if dic[curr] < dic[s[i+1]]:
                result -= dic[curr]
            else:
                result += dic[curr]
        result += dic[s[-1]]
        return result