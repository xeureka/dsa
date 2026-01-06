class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]


        for i in range(n + 1):
            dp[i][m] = n - i
        for j in range(m + 1):
            dp[n][j] = m - j

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if a[i] == b[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1])

        ans = []
        i, j = 0, 0
        while i < n or j < m:
            if i < n and j < m and a[i] == b[j]:
                ans.append(a[i])
                i += 1
                j += 1
            elif i < n and (j == m or dp[i + 1][j] <= dp[i][j + 1]):
                ans.append(a[i])
                i += 1
            else:
                ans.append(b[j])
                j += 1

        return "".join(ans)