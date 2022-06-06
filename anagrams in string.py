class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ds1 = {}
        for ch in s1:
            ds1[ch] = ds1.get(ch, 0) + 1

        ds2 = {}
        ls1, ls2 = len(s1), len(s2)
        if ls1 > ls2:
            return False

        for i in range(ls1 - 1):
            ds2[s2[i]] = ds2.get(s2[i], 0) + 1

        start, i = 0, ls1 - 1
        while i < ls2:
            ds2[s2[i]] = ds2.get(s2[i], 0) + 1
            if ds1 == ds2:
                return True
            if ds2[s2[start]] == 1:
                del ds2[s2[start]]
            else:
                ds2[s2[start]] -= 1
            start, i = start + 1, i + 1

        return False
