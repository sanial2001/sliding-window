class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        sums, ans = 0, 0
        for i in range(len(nums)):
            sums += nums[i]
            if sums % k in d:
                ans += d[sums % k]
            d[sums % k] = d.get(sums % k, 0) + 1
        return ans
