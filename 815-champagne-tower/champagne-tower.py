class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        n = 101
        dp = [0] * n
        dp[0] = poured
        cnt = 0
        for i in range(1, n):
            if cnt == query_row:
                return min(dp[query_glass], 1)
            for j in range(i - 1, -1, -1):
                calc = max((dp[j] - 1) / 2, 0)
                if dp[j] >= 1:
                    dp[j + 1] += calc
                    dp[j] = calc
                else:
                    dp[j] = 0
                    
            cnt += 1