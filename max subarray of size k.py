def solve(nums, k):
    n = len(nums)
    temp = sum(nums[0:k])
    ans = 0
    i, j = 0, k
    while j < n:
        temp = temp - nums[i] + nums[j]
        ans = max(ans, temp)
        i, j = i+1, j+1
    return ans


if __name__ == '__main__':
    print(solve(nums=[2, 5, 1, 8, 2, 9, 1], k=3))
