class Solution:
    def minOperations(self, s: str) -> int:
        opr_zero = 0

        for index,char in enumerate(s):
            expected = '01' [index & 1]

            if char != expected:
                opr_zero += 1

        opr_one = len(s) - opr_zero
        return min(opr_zero,opr_one)
