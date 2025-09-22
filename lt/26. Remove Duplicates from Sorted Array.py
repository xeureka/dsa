'''
 - nums sorted in non-decreasing order, remove duplicates in place such that each
 unique elemnt appeats only once.
 - The relative order of elements shoud ke kept the same
 - The return the number of unique elemets in nums

 Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

 '''


def solution(nums: list):
    j = 1
    n = len(nums)

    for i in range(1,n):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1

    return j


