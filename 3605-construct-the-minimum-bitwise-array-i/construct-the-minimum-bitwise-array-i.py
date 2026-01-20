class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [next((i for i in xrange(x) if i|(i+1) == x), -1) for x in nums]