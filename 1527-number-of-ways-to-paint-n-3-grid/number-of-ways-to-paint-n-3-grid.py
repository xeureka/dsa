class Solution:
    def numOfWays(self, n: int) -> int:
        forms = [
            "RYR", "YRY", "GRY", "RYG",
            "YRG", "GRG", "RGR", "YGR",
            "GYR", "RGY", "YGY", "GYG" 
        ]
        mod = 10**9 + 7
        table = defaultdict(list)
        for i in range(len(forms)):
            for j in range(i + 1, len(forms)):
                connect = True
                for k in range(3):
                    if forms[i][k] == forms[j][k]:
                        connect = False
                if connect:
                    table[i].append(j)
                    table[j].append(i)

        dp = [1] * 12
        me = [0] * 12
        for i in range(n - 2, -1, -1):
            for cur in range(12):
                for lij in table[cur]:
                    me[cur] += dp[lij]
                    me[cur] %= mod
            for i in range(12):
                dp[i] = me[i]
                me[i] = 0
        
        return sum(dp) % mod