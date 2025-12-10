class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
    
        sorted_count = sorted(counter.keys(), key = lambda x:counter[x],reverse=True)
        return sorted_count[:k]