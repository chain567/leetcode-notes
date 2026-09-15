class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        n = len(nums)
        count = 0
        left, right = 0, 1
        while right < n-1:
            if nums[right+1]-nums[right] == nums[right]-nums[right-1]:
                right += 1
            else:
                length = right - left + 1
                count += (length-1) * (length-2)/2
                if right < n - 1:
                    left = right
                right += 1
                
        length = right - left + 1
        count += (length-1) * (length-2)/2
        return count