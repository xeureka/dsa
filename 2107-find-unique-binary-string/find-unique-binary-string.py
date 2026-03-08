class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        results = set()
        n = len(nums[0])

        for i in range(2**n):
            binary_str = format(i,f'0{n}b')
            results.add(binary_str)

        for j in results:
            if j not in nums:
                return j
