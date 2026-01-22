class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for _ in range(n):
            sor = True
            mn = [float('inf'), -1, -1]
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    sor = False
                if nums[i] + nums[i - 1] < mn[0]:
                    mn = [nums[i] + nums[i - 1], i - 1, i]
            if sor:
                return ans
            nums.pop(mn[-1])
            nums[mn[1]] = mn[0]
            ans += 1