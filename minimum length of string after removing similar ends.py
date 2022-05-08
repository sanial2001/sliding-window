class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        i, j = 0, n - 1

        while i < j and s[i] == s[j]:
            ch = s[i]
            while i < n and s[i] == ch:
                i += 1
            while j > 0 and s[j] == ch:
                j -= 1

        ans = j - i + 1
        return 0 if ans < 0 else ans
