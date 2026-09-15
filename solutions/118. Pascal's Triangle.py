class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1] * i for i in range(1, numRows+1)]
        for num in range(numRows):
            for i in range(1, num):
                    result[num][i] = result[num-1][i-1] + result[num-1][i]

        return result
