class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, 0
        n = len(nums)
        curr = nums[left]
        result = 0
        while right < n:
            while left <= right and curr >= k:
                curr /= nums[left]
                left += 1
            result += right - left + 1
            right += 1
            if right == n:
                break
            curr *= nums[right]
        return result