class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def checker(mid):
            above = 0.0
            below = 0.0

            for x, y, l in squares:
                if y >= mid:
                    above += l * l
                elif y + l <= mid:
                    below += l * l
                else:
                    above += (y + l - mid) * l
                    below += (mid - y) * l

            return above - below
        l, r = 0, 1e9
        while (r - l) > 1e-5:
            mid = (r + l) / 2
            if checker(mid) > 0:
                l = mid
            else:
                r = mid
        return r
