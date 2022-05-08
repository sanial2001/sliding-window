class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        start = 0
        t, ans = set(), 0
        for i in range(n):
            while s[i] in t:
                t.remove(s[start])
                start += 1
            t.add(s[i])
            ans = max(ans, len(t))
        return ans
