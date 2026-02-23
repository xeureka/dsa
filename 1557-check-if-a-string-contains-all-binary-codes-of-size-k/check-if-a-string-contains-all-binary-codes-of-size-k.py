class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        checker = set()
        cur = deque()
        l = 0
        for r in range(len(s)):
            cur.append(s[r])
            if len(cur) == k:
                checker.add("".join(cur))
                cur.popleft()
        return len(checker) == (1 << k)