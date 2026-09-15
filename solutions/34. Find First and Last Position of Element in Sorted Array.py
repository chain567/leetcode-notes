class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums) - 1
        if len(nums) < 1:
            return [-1,-1]
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                break
        if low > high:
            return [-1,-1]
        
        left_max = mid
        left_low = low
        left_start = 0
        while left_low <= left_max and mid != 0:
            left_start = (left_low + left_max) // 2
            if nums[left_start] < target:
                left_low = left_start + 1
            elif nums[left_start] == target and left_start > low and nums[left_start-1] == target:
                left_max = left_start-1
            else:
                break
        
        right_max = high
        right_low = mid
        right_start = high
        while right_low <= right_max and mid != high:
            right_start = (right_low + right_max) // 2
            if nums[right_start] > target:
                right_max = right_start - 1
            elif nums[right_start] == target and right_start < high and nums[right_start+1] == target:
                right_low = right_start+1
            else:
                break
        return [left_start, right_start]

'''
nums = [2,2]
target = 2
print(Solution().searchRange(nums, target))
'''