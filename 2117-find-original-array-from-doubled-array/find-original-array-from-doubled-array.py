class Solution:
    # in a sorted order, first element must be part of the original.
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        original = [changed[0]]
        index = 0
        for i in range(1, len(changed)):
            num = changed[i]
            if index < len(original) and original[index] * 2 == num:
                index += 1
                continue
            original.append(num)
        if index == len(original):
            return original
        return []