class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lib = {}
        for i in range(len(nums)):
            curr = nums[i]
            if curr in lib:
                lib[curr] = None
            else:
                lib[curr] = 1
        
        print(lib)
        for key, val in lib.items():
            if val == 1:
                return key
'''
nums = [2,2,1]
print(Solution().singleNumber(nums))
'''