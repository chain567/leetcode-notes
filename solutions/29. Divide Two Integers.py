class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = (dividend < 0) ^ (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        ans = 0
        while a >= b:
            temp = b
            multiple = 1
            while temp <= a:
                temp <<= 1
                multiple <<= 1
            a -= temp >> 1
            ans += multiple >> 1
        if neg:
            ans = 0 - ans
        if ans > 2147483647:
            ans = 2147483647
        if ans < -2147483648:
            ans = -2147483648
        return ans