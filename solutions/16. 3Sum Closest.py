class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = nums[0] + nums[1] + nums[2]
        new_nums = sorted(nums)
        for i in range(len(new_nums)):
            j = i + 1
            k = len(new_nums) - 1
            while j < k:
                curr = new_nums[i] + new_nums[j] + new_nums[k]
                if abs(curr-target) < abs(closest-target):
                    closest = curr
                if curr > target:
                    k -= 1
                elif curr < target:
                    j += 1
                else:
                    return curr
        return closest