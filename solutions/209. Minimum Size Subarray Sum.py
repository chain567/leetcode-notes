class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        min_len = float("inf")
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            while curr >= target:
                if i - low + 1 < min_len:
                    min_len = i - low + 1
                curr -= nums[low]
                low += 1
        return 0 if min_len == float("inf") else min_len