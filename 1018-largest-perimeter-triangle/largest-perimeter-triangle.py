class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = 0
        nums.sort(reverse = True)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2] :
                maxi = max(maxi,nums[i] + nums[i+1] + nums[i+2])
        return maxi


        