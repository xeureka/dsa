class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        check = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
        ans = 0
        for num in range(left, right + 1):
            ans += (num.bit_count() in check)
        return ans