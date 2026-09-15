class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums) - 1
        result = []
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                k = j + 1
                p = n
                while k < p:
                    curr = nums[i] + nums[j] + nums[k] + nums[p]
                    if curr == target:
                        add = [nums[i], nums[j], nums[k], nums[p]]
                        if add not in result:
                            result.append(add)
                        p -= 1
                        k += 1
                    elif curr > target:
                        p -= 1
                    else:
                        k += 1

        return result 