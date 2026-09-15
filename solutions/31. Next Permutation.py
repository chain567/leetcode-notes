class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        sort = True
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                sort = False
        if sort:
            nums[:] = nums[::-1]
            return
        h = len(nums)-1
        # find digits to swap
        while nums[h] <= nums[h-1]:
            h -= 1
        h -= 1
        change = nums[h:]
        tar = change[0]
        closest = 1
        for dig in range(2, len(change)):
            if change[dig] < change[closest] and change[dig] > tar:
                closest = dig
        temp = change[closest]
        change[closest] = tar
        change[0] = temp

        change = [change[0]] + sorted(change[1:])

        nums[:] = nums[:h] + change

'''
nums = [2,2,7,5,4,3,2,2,1] # [4,3,5,4,2]
Solution().nextPermutation(nums) # [4,4,2,3,5] ， [2,3,1,2,2,2,4,5,7]
print(nums)
'''