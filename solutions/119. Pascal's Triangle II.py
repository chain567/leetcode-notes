import math

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        else:
            result = [1] * (rowIndex+1)
            for i in range(1, rowIndex):
                curr = math.factorial(rowIndex) / (math.factorial(i)*math.factorial(rowIndex-i))
                result[i] = curr
            return result
