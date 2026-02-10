class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nm = {}
        for i, num in enumerate(nums):
            nm[num] = i
        
        for i,num in enumerate(nums):
            y = target-num 
            if y in nm and nm[y] != i:
                return [i,nm[y]]