class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        if target > coins[-1]:
            coins.append(target + 1)
        ans = 0
        cur = 0
        i = 0
        while i < len(coins):
            coin = coins[i]
            if cur + 1 >= coin:
                cur += coin
                i += 1
            else:
                cur += (cur + 1)
                ans += 1
        return ans