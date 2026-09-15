class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        result += 'M' * (num // 1000)
        num %= 1000
        hun = num // 100
        num %= 100
        if hun == 4:
            result += 'CD'
        elif hun == 9:
            result += 'CM'
        elif hun >= 5:
            result += 'D' + 'C' * (hun - 5)
        else:
            result += 'C' * hun

        ten = num // 10
        num %= 10
        if ten == 4:
            result += 'XL'
        elif ten == 9:
            result += 'XC'
        elif ten >= 5:
            result += 'L' + 'X' * (ten - 5) 
        else:
            result += 'X' * ten
        
        one = num
        if one == 4:
            result += 'IV'
        elif one == 9:
            result += 'IX'
        elif one >= 5:
            result += 'V' + 'I' * (one - 5)
        else:
            result += 'I' * one

        return result

'''
My solution is very fast but not good. Since num is between 0 and 3999, so my solution works.
However, there are better solutions.
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        Roman = ""
        storeIntRoman = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        for i in range(len(storeIntRoman)):
            while num >= storeIntRoman[i][0]:
                Roman += storeIntRoman[i][1]
                num -= storeIntRoman[i][0]
        return Roman