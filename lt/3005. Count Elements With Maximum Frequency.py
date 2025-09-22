'''
 - You are given an array nums consisting of postive integers.
 - Return the total frequencices of elemtns in nums such that those elemnts have
 maximum frequency
 - the frequency of an elemnts is the number of occurences of that elent in the array

'''

def solution(nums: list):
    hashmap = dict()

    for i in nums:
        if not i in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    for val,freq in