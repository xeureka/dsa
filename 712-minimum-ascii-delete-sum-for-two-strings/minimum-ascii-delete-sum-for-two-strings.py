                                            
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    mew = 0
                    if i + 1 == n:
                        for cur in range(j + 1, m):
                            mew += ord(s2[cur])
                    elif j + 1 == m:
                        for cur in range(i + 1, n):
                            mew += ord(s1[cur])
                    else:
                        mew += dp[i + 1][j + 1]
                    dp[i][j] = mew
                else:
                    one = ord(s1[i])
                    if i + 1 == n:
                        for cur in range(j, m):
                            one += ord(s2[cur])
                    else:
                        one += dp[i + 1][j]
                    two = ord(s2[j])
                    if j + 1 == m:
                        for cur in range(i, n):
                            two += ord(s1[cur])
                    else:
                        two += dp[i][j + 1]
                    dp[i][j] = min(one, two)
        return dp[0][0]
