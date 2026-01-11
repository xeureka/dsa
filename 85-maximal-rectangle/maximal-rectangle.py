class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        nums = [0] * (m + 1)
        ans = 0
        def get_max():
            nonlocal ans
            stack = []
            for i in range(len(nums)):
                while stack and nums[stack[-1]] > nums[i]:
                    cur = stack.pop()
                    width = i - (stack[-1] if stack else -1) - 1
                    ans = max(ans, nums[cur] * width)
                stack.append(i)

        for r in range(n - 1, -1, -1):
            for c in range(m):
                nums[c] = nums[c] + 1 if matrix[r][c] == "1" else 0
            get_max()
        return ans