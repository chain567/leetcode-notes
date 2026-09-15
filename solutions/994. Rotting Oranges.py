from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        num = 0
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        time = 0
        if num == 0:
            return time
        while queue and num > 0:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                for di in direction:
                    check = (curr[0]+di[0], curr[1]+di[1])
                    if check[0] <= m-1 and check[0] >= 0 and check[1] >= 0 and check[1] <= n-1 and grid[check[0]][check[1]] == 1:
                        grid[check[0]][check[1]] = 2
                        num -= 1
                        queue.append(check)
            time += 1
            
        if num == 0:
            return time
        else:
            return -1