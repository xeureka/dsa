class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = {}
        for i in range(n):
            count[i] = 0
        for city_1, city_2 in roads:
            count[city_1] += 1
            count[city_2] += 1
        
        total = 0
        curr_ind = 1
        for count in sorted(count.values()):
            total += count * curr_ind
            curr_ind += 1
        return total
