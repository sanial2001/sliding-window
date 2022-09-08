class Solution:
    def solve(self, nums):
        n = len(nums)
        i, start, ans = 0, 0, 0
        sums, d = 0, collections.defaultdict(int)
        while i < n:
            sums += nums[i]
            d[nums[i]] += 1
            while d[nums[i]] > 1:
                d[nums[start]] -= 1
                sums -= nums[start]
                start += 1
            ans = max(ans, sums)
            i += 1
        return ans
