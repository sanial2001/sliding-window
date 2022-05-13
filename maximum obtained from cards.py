class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        window = n - k
        total = sum(nums)
        i, j = 0, window
        sums = sum(nums[:window])
        ans = total - sums

        while j < n:
            sums = sums + (nums[j] - nums[i])
            ans = max(ans, total - sums)
            i, j = i + 1, j + 1

        return ans
