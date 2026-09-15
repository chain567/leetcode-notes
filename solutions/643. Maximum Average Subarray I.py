class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left, right = 0, k-1
        n = len(nums)
        curr = sum(nums[:k])
        largest = curr
        while right < n-1:
            curr = curr - nums[left] + nums[right+1]
            largest = max(largest, curr)
            right += 1
            left += 1       
        return largest/float(k)