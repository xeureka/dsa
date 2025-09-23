'''

- nums and val
- remove all occrences of val in nums in place (return the)

'''

def solution(nums: list, val:int):
    answer = []

    for i in nums:
        if i != nums:
            answer.append(i)

    return len(nums)


