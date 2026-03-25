class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        @cache
        def dfs(r, c):
            if r == n - 1 and c == m - 1:
                return (grid[r][c], grid[r][c])

            max_val = float('-inf')
            min_val = float('inf')

            if r + 1 < n:
                mx, mn = dfs(r + 1, c)
                candidates = [grid[r][c] * mx, grid[r][c] * mn]
                max_val = max(max_val, max(candidates))
                min_val = min(min_val, min(candidates))

            if c + 1 < m:
                mx, mn = dfs(r, c + 1)
                candidates = [grid[r][c] * mx, grid[r][c] * mn]
                max_val = max(max_val, max(candidates))
                min_val = min(min_val, min(candidates))

            return (max_val, min_val)

        res, _ = dfs(0, 0)

        MOD = 10**9 + 7
        return res % MOD if res >= 0 else -1