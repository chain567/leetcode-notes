''' Solution 1: θ(n*k)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            num = min(i+k+1, len(nums))
            for j in range(i+1, num):
                if nums[i] == nums[j]:
                    return True            
        return False
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        arr = {}        
        for i in range(len(nums)):
            curr = nums[i]
            if curr not in arr:
                arr[curr] = i
            else:
                if i - arr[curr] <= k:
                    return True
                else:
                    arr[curr] = i
        return False