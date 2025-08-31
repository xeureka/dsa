class Solution(object):
    def trailingZeros(self, n):
        count = 0
        divisor = 5

        while n>= divisor:
            count += n // divisor
            divisor += 5

        return count