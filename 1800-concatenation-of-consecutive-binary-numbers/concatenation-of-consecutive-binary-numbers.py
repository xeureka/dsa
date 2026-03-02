class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        cur = 0
        for num in range(1, n + 1):
            for bit in range(num.bit_length() - 1, -1, -1):
                cur <<= 1
                if (num & (1 << bit)):
                    cur |= 1
                cur %= mod
        return cur