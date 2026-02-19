class Solution: 
    def hasAlternatingBits(self, n: int) -> bool: 
        for i in range(1, n.bit_length()): 
            if (bool(n & (1 << i)) == bool(n & (1 << (i - 1)))): 
                return False 
        return True