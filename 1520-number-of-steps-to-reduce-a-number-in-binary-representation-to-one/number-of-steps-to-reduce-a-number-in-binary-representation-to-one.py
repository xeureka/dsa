class Solution:
    def numSteps(self, s: str) -> int:
        new = list(reversed(s))
        i = 0
        ans = 0
        while i < len(new) - 1 or new[i] == '0':
            if new[i] == "1":
                for j in range(i, len(new)):
                    if new[j] == "0":
                        new[j] = "1"
                        break
                    new[j] = "0"
                else:
                    new.append("1")
            else:
                i += 1
            ans += 1
        return ans