class Solution:
    def groupThePeople(self, group: List[int]) -> List[List[int]]:
        table = defaultdict(list)
        for i, num in enumerate(group):
            table[num].append(i)
        
        ans = []
        for k, v in table.items():
            ans.append([])
            for num in v:
                ans[-1].append(num)
                if len(ans[-1]) == k:
                    ans.append([])
            if not ans[-1]:
                ans.pop()
        return ans