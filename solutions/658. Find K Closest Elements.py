class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(arr)
        left, right = 0, n-1
        while right - left + 1 > k:
            if abs(arr[right]-x) >= abs(arr[left]-x):
                right -= 1
            else:
                left += 1
        return arr[left:left+k]