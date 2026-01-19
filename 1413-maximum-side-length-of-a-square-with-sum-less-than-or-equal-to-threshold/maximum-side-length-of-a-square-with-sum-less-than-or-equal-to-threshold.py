class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])
        pre = [[0] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                pre[r][c] += (
                    mat[r][c] + 
                    (pre[r][c - 1] if c else 0) + 
                    (pre[r - 1][c] if r else 0) - 
                    (pre[r - 1][c - 1] if r and c else 0)
                )
        def checker(cur):
            mine = float('inf')
            for r in range(cur - 1, n):
                for c in range(cur - 1, m):
                    calc = (
                        pre[r][c] - 
                        (pre[r - cur][c] if r - cur >= 0 else 0) - 
                        (pre[r][c - cur] if c - cur >= 0 else 0) +
                        (pre[r - cur][c - cur] if r - cur >= 0 and c - cur >= 0 else 0)
                    )
                    mine = min(mine, calc)
            return mine <= threshold
            
        l, r = 0, min(n, m)
        while r >= l:
            mid = (l + r) // 2
            if checker(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r                 