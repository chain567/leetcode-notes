class Solution:
    def canJump(self, nums: list[int]) -> bool:
        gas = nums[0]
        for i in range(1, len(nums)):
            if gas == 0:
                return False
            gas = max(gas-1, nums[i])
        return True