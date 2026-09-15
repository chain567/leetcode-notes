class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = [0] * len(digits)
        if digits[-1] == 9:
            incr = 1
            result[-1] = 0
        else:
            incr = 0
            result[-1] = digits[-1] + 1
        ind = len(digits)-2
        while ind >= 0:
            dig = digits[ind] + incr
            incr = dig // 10
            dig -= incr * 10
            result[ind] = dig
            ind -= 1
        if incr != 0:
            return [incr] + result
        else:
            return result