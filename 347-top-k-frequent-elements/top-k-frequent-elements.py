class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            counter = Counter(nums)
            ordered = sorted(counter.items(), key=lambda item: item[1],reverse=True)
            
            ans = []
            
            for i in range(k):
                ans.append(ordered[i][0])
            
            return ans