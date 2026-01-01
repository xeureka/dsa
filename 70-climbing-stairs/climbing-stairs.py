class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.memo = {}
        return self.recur(n)
    def recur(self,n):
        if n < 3:
            return n  
        if n not in self.memo:
            self.memo[n] = self.recur(n-1) + self.recur(n-2)
        return self.memo[n]