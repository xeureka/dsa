class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        table = Counter(nums)
        ans = []
        while len(table):
            cur = list(table.keys())
            for k in cur:
                table[k] -= 1
                if not table[k]:
                    del table[k]
            ans.append(cur)
        return ans