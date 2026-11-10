class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        ans = 0
        rows, cols = len(grid), len(grid[0])
        fo = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    fo += 1
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]
        while q:
            x, y, time = q.popleft()
            ans = max(time, ans)
            for dr, dc in directions:
                i, j = x+dr, y+dc
                if 0<=i<rows and 0<=j<cols and grid[i][j] == 1:
                    grid[i][j] = 2
                    fo -= 1
                    q.append((i, j, time+1))
        return ans if fo == 0 else -1