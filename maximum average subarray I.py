class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums, ans = 0, float("-inf")
        i = 0
        for j in range(len(nums)):
            sums += nums[j]
            if j - i + 1 == k:
                ans = max(ans, sums)
                sums -= nums[i]
                i = i + 1
        return ans / k
