class Solution:
    def numSub(self, s: str) -> int:
        prev_ones = total = 0
        for c in s:
            if c == "1":
                prev_ones += 1
            else:
                total += (prev_ones * (prev_ones + 1)) // 2
                prev_ones = 0
        return( total + (prev_ones * (prev_ones + 1)) // 2) % (10 ** 9 + 7)