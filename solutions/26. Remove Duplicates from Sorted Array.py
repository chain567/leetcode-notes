class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        j = 1
        for i in range(n-1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i+1]
                j += 1
        return j