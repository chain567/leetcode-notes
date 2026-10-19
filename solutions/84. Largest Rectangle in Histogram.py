class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        for idx, h in enumerate(heights):
            prev_idx = idx
            while stack and stack[-1][0] > h:
                prev_h, prev_idx = stack.pop()
                max_area = max(max_area, prev_h * (idx - prev_idx))
            stack.append((h, prev_idx))
        while stack:
            prev_h, prev_idx = stack.pop()
            max_area = max(max_area, prev_h * (len(heights)-prev_idx))
        return max_area
                