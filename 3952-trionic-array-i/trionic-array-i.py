class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 4 or nums[0] > nums[1]:
            return False
        ans = [nums[0]]
        for i in range(1, len(nums)):
            if (len(ans) % 2 and nums[i] > ans[-1]) or (len(ans) % 2 == 0 and nums[i] < ans[-1]):
                ans[-1] = nums[i]
            elif nums[i] == ans[-1]:
                return False
            else:
                ans.append(nums[i])
            print(ans)
        return len(ans) == 3