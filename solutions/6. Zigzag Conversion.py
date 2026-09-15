class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        elif numRows == 2:
            return s[::numRows] + s[1::numRows]
        n = len(s)
        lib = [[] for _ in range(numRows)]
        inverse = False
        i = 0
        while i < n:
            curr = s[i]
            if not inverse:
                for j in range(numRows):
                    if i == n:
                        break
                    lib[j].append(s[i])
                    i += 1
                inverse = True
            else:
                for k in range(numRows-2, 0, -1):
                    if i == n:
                        break
                    lib[k].append(s[i])
                    i += 1
                inverse = False
        result = ""
        for arr in lib:
            arr_str = "".join(arr)
            result += arr_str
        return result