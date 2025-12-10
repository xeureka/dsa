class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hm = set()
        for i in nums:
            if i in hm:
                return True
            else:
                hm.add(i)
        return False

        