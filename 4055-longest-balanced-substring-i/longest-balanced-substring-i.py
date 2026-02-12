class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            cur = defaultdict(int)
            for j in range(i, len(s)):
                cur[s[j]] += 1
                if len(set(cur.values())) == 1:
                    ans = max(j - i + 1, ans)
        return ans