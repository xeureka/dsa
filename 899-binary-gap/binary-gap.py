class Solution:
    def binaryGap(self, n: int) -> int:
        prev = -1
        ans = 0
        for bit in range(31):
            if n & (1 << bit):
                if prev >= 0:
                    ans = max(ans, bit - prev)
                prev = bit
        return ans