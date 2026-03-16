class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        d = set() 
        
        for num in nums:
            if num in d:
                return True
            else: 
                d.add(num)
        return False
