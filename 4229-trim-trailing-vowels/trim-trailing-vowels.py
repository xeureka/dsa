class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = set("aeiou")

        s_set = list(s)

        for i in range(len(s) - 1, -1, -1):
            if s_set[i] in vowels:
                del s_set[i]
            else:
                break

        return "".join(s_set)
