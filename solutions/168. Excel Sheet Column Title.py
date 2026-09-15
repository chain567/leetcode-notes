class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        num = 0
        result = ''
        while columnNumber > 0:
            curr = columnNumber % 26
            if curr == 0:
                curr = 26
                columnNumber = (columnNumber-26) // 26
            else:
                columnNumber = columnNumber // 26
            result = chr(curr+64) + result
        return result
        
            