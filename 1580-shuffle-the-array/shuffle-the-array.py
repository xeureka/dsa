class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left,right = 0,n
        ans = []
        count = 0
        
        for _ in range(len(nums)):
            if count % 2 == 0:
                ans.append(nums[left])
                left += 1
                count += 1
            else:
                ans.append(nums[right])
                right += 1
                count += 1
        return ans
                