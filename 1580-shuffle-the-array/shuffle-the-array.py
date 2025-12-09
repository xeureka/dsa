class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        arr1 = nums[:n]
        arr2 = nums[n:]
        new = list()
        for i in range(len(arr1)):
            new.append(arr1[i])
            new.append(arr2[i])
        return new