class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        s = answerKey[:]
        d = {}
        ans, i = 0, 0
        for j in range(len(s)):
            d[s[j]] = d.get(s[j], 0) + 1
            cnt = (j - i + 1) - max(d.values())
            while cnt > k:
                d[s[i]] -= 1
                i = i + 1
                cnt = (j - i + 1) - max(d.values())
            ans = max(ans, j - i + 1)
        return ans
