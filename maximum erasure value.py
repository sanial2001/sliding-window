class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        t, sums, ans = set(), 0, 0
        for i in range(n):
            while t and nums[i] in t:
                sums -= nums[start]
                t.remove(nums[start])
                start += 1
            t.add(nums[i])
            sums += nums[i]
            ans = max(ans, sums)
        return ans
