class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        a = {}
        for word in strs:
            s = "".join(sorted(word))
            if s in a:
                a[s].append(word)
            else:
                a[s] = [word]
        
        res = list(a.values())
        return res
        