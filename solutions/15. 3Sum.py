class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        new_nums = sorted(nums)
        for i in range(0, len(nums)-1):
            j = i+1
            k = len(nums)-1
            curr = new_nums[i]
            num_sum = curr + new_nums[j] + new_nums[k]
            while j < k:
                if num_sum == 0:
                    add_num = sorted([new_nums[i], new_nums[j], new_nums[k]])
                    if add_num not in result:
                        result.append(add_num)
                    k -= 1
                    j += 1
                elif num_sum > 0:
                    k -= 1
                else:
                    j += 1
                num_sum = curr + new_nums[j] + new_nums[k]
        return result