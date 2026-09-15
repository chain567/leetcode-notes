class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_vol = 0

        while left < right:
            curr_vol = min(height[left], height[right]) * (right - left)
            if curr_vol > max_vol:
                max_vol = curr_vol
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_vol  