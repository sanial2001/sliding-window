class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        ans = 1 if sum(arr[:k]) // k >= threshold else 0
        i, j = 0, k
        s = sum(arr[:k])
        while j < n:
            s = s - arr[i] + arr[j]
            ans = ans + (1 if s // k >= threshold else 0)
            i, j = i + 1, j + 1
        return ans
