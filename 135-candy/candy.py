class Solution:
    def candy(self, rate: List[int]) -> int:
        n = len(rate)
        suf = [1]
        for i in range(n - 2, -1, -1):
            if rate[i] > rate[i + 1]:
                suf.append(suf[-1] + 1)
            else:
                suf.append(1)
        suf.reverse()
        ans = 0
        pre = 1
        for i in range(n):
            if i and rate[i] > rate[i - 1]:
                pre += 1
            elif i:
                pre = 1
            ans += max(pre, suf[i])
        return ans