class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        cur = 1
        for coin in coins:
            if cur >= coin:
                cur += coin
        return cur