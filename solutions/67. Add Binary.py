class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ind = 0
        lena = len(a) - 1
        lenb = len(b) - 1
        result = ""
        while lena >= 0 and lenb >= 0:
            curr = int(a[lena]) + int(b[lenb]) + ind
            ind = curr // 2
            curr -= 2*ind
            result = str(curr) + result
            lena -= 1
            lenb -= 1
        while lena >= 0:
            curr = int(a[lena]) + ind
            ind = curr // 2
            curr -= 2*ind
            result = str(curr) + result
            lena -= 1
        while lenb >= 0:
            curr = int(b[lenb]) + ind
            ind = curr // 2
            curr -= 2*ind
            result = str(curr) + result
            lenb -= 1
        if ind > 0:
            result = str(ind) + result
        return result
        