def solve(nums, k):
    start, sums = 0, 0
    ans = 0
    for i in range(len(nums)):
        sums += nums[i]
        while sums > k:
            sums = sums-nums[start]
            start = start+1
        if sums == k:
            #print(i-start+1)
            ans = max(i-start+1, ans)
    print(ans)


if __name__ == '__main__':
    solve(nums=[4, 1, 1, 1, 2, 3, 5], k=5)
