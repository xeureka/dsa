class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def calc(num):
            i = 0
            while num & (1 << i):
                i += 1
            return num ^ (1 << (i - 1))
        return [calc(num) if num & 1 else -1 for num in nums]