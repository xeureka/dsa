class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, ans = 0, len(nums)
        for r in range(len(nums)):
            while nums[r] > k * nums[l]:
                l += 1
            ans = min(ans, len(nums) - (r - l + 1))
        return ans