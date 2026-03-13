class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque([(0, -1)])
        ans = float('inf')
        total = 0
        for i, num in enumerate(nums):
            total += num
            while q and q[-1][0] >= total:
                q.pop()
            q.append((total, i))
            while q and total - q[0][0] >= k:
                ans = min(ans, i - q[0][-1])
                q.popleft()
        
        return ans if ans != float("inf") else -1