class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = [[], float('inf')]
        for i in range(1, len(arr)):
            cur = arr[i] - arr[i - 1]
            if cur < ans[1]:
                ans = [[[arr[i - 1], arr[i]]], cur]
            elif cur == ans[1]:
                ans[0].append([arr[i - 1], arr[i]])
        return ans[0]