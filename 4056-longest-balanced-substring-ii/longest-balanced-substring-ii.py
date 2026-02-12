class Solution:
    def longestBalanced(self, s: str) -> int:
        def for_one(ch):
            ans = 0
            cur = 0
            for r in range(len(s)):
                if ch == s[r]:
                    cur += 1
                else:
                    cur = 0
                ans = max(ans, cur)
            return ans
        def for_two(start, end):
            ans = 0
            table = defaultdict(int)
            table[0] = -1
            cur = 0
            for r, ch in enumerate(s):
                if ch == start:
                    cur += 1
                elif ch == end:
                    cur -= 1
                else:
                    cur = 0
                    table.clear()
                    table[0] = r
                    continue
                if cur in table:
                    ans = max(ans, r - table[cur])
                else:
                    table[cur] = r
            return ans

        # print(for_two("a", "c"), for_one("b"))
        eskahun = max([
            for_one("a"), for_one("b"), for_one("c"),
            for_two("a", "b"), for_two("a", "c"), for_two("c", "b")
        ])
        def for_three():
            if len(s) < 3:
                return 0
            def calc(s):
                count = Counter()
                res = 0
                
                prev = [0,0,0]
                count[tuple(prev)] = -3
                for i in range(0,len(s)-2,3):


                    prev[ord(s[i]) - ord("a")] += 1
                    prev[ord(s[i+1]) - ord("a")] += 1
                    prev[ord(s[i+2]) - ord("a")] += 1

                    for j in range(3):
                        prev[j] -= 1

                    cur = tuple(prev)
                    if cur in count:
                        res = max(res, i - count[cur])
                    else:
                        count[cur] = i

                return res
            return max(calc(s[1:]),calc(s),calc(s[2:]))
        # print(for_three())
        return max(for_three(), eskahun)
        