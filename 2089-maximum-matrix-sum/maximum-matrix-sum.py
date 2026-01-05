class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        total, neg = 0, 0
        mn = float('inf')
        for r in range(n):
            for c in range(n):
                total += abs(matrix[r][c])
                mn = min(mn, abs(matrix[r][c]))
                if matrix[r][c] < 0:
                    neg += 1
        if neg % 2:
            total -= mn * 2
        return total