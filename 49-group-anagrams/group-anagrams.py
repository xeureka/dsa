class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            sw = ''.join(sorted(word))
            d[sw].append(word)

        return list(d.values())        