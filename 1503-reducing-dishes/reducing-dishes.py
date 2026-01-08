class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        sat.sort()
        @cache
        def back(idx, cur):
            if idx == len(sat):
                return 0
            take = cur * sat[idx] + back(idx + 1, cur + 1)
            nottake = back(idx + 1, cur)
            return max(take, nottake)
        return back(0, 1)