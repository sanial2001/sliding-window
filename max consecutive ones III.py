class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt, ans, i = 0, 0, 0
        for j in range(len(nums)):
            if nums[j] == 0:
                cnt += 1
            while cnt > k:
                if nums[i] == 0:
                    cnt -= 1
                i = i + 1
            ans = max(ans, j - i + 1)
        return ans
