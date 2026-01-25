class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min([nums[r] - nums[r - k + 1] for r in range(k - 1, len(nums))])