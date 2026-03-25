class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        prev, tot, n, m = 0, sum([sum(row) for row in grid]), len(grid), len(grid[0])
        for r in range(n):
            for c in range(m):
                prev += grid[r][c]
                grid[r][c] += ((grid[r-1][c] if r > 0 else 0) + (grid[r][c-1] if c > 0 else 0) -(grid[r-1][c-1] if min(r, c) > 0 else 0))
                if (c == m - 1 and prev == tot - prev) or (r == n - 1 and grid[r][c] == tot - grid[r][c]): return True
        return False