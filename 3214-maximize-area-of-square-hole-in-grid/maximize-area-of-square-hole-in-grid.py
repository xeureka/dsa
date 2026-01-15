class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
            def max_gap(arr):
                arr.sort()
                result = l = 1
                for i in range(len(arr)):
                    l += 1
                    result = max(result, l)
                    if i+1 != len(arr) and arr[i+1] != arr[i]+1:
                        l = 1
                return result

            return min(max_gap(hBars), max_gap(vBars))**2