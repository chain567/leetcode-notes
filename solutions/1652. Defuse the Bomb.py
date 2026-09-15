class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        if k == 0:
            return [0] * n
        result = [0] * n
        curr = 0
        left = 1 if k > 0 else (k + n) % n
        right = (k + n) % n if k > 0 else n-1
        for i in range(left, right + 1):
            curr += code[i]
        for j in range(n):
            result[j] = curr
            right = (right + 1) % n
            curr = curr - code[left] + code[right]
            left = (left + 1) % n
            print(curr, code[left], code[right])
        return result