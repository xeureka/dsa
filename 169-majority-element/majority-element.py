class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        maj = ceil(len(nums) / 2)
        for i,j in counter.items():
            if j >= maj:
                return i