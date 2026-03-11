class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_n = bin(n)[2:]
        new = ""
        for i in bin_n:
            if i == "0":
                new += "1"
            else:
                new += "0"
        return int(new,2)
