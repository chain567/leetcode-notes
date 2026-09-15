# https://leetcode.com/problems/reverse-integer/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        num = x
        arr = []
        result = 0
        minus = False
        if num < 0:
            minus = True
            num *= -1
        while num > 0:
            arr.append(num % 10)
            num = num // 10
        for i in range(len(arr)):
            result = result * 10 + arr[i]
        result = -1 * result if minus else result
        if result > 2 ** 31 - 1 or result < - 2 ** 31:
            return 0
        else:
            return result