class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        return self.binarySearch(nums, 0, len(nums)-1)
    def binarySearch(self, nums, l, r):
        if l == r:
            return l
        mid = (l+r) // 2
        if nums[mid] > nums[mid+1]:
            return self.binarySearch(nums,l,mid) # down the slope
        return self.binarySearch(nums, mid+1, r) # up the slope