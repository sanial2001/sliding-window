class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans, prev = 0, 0
        i, j = 0, 0
        n = len(nums)

        for j in range(n):
            if left <= nums[j] <= right:
                prev = (j - i + 1)
                ans += prev
            elif nums[j] < left:
                ans += prev
            else:
                i, prev = j + 1, 0

        return ans
