class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        table = defaultdict(list)
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[j] - nums[i]) % 2 or not (nums[j] - nums[i]): continue
                table[nums[j] - nums[i]].append((i, j))
        
        for k, v in table.items():
            check = set()
            low = []
            for a, b in v:
                if a not in check and b not in check:
                    check.add(a)
                    low.append(nums[a] + (k // 2))
                    check.add(b)
            if len(check) == len(nums):
                return low