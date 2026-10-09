class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n <= 1:
            return nums
        mid = n // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(nums, left, right)
    def merge(self, nums, left, right):
        l, r = 0, 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        while l < len(left):
            result.append(left[l])
            l += 1
        while r < len(right):
            result.append(right[r])
            r += 1
        return result
