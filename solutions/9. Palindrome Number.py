class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        num = x
        length = 0
        test = num
        while test >= 10:
            test = test // 10
            length += 1

        while num > 0:
            last = num % 10
            first = num // 10 ** length
            if last != first:
                return False
            num -= first* 10 ** length
            num = num // 10
            length -= 2
        return True