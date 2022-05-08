class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        t = [-1 for _ in range(n)]
        sums, i = 0, 0
        radius = 2 * k + 1
        for j in range(n):
            sums += nums[j]
            if j - i + 1 == radius:
                t[j - k] = sums // radius
                sums -= nums[i]
                i = i + 1
        return t
