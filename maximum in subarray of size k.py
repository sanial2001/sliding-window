def solve(nums, k):
    q, res = [], []
    for i, num in enumerate(nums):
        while q and num > nums[q[-1]]:
            q.pop()
        q.append(i)
        if i == q[0] + k:
            q.pop(0)
        if i >= k - 1:
            res.append(nums[q[0]])
    return res


if __name__ == '__main__':
    print(solve(nums=[1, 2, 3, 5, 3, 7, 1, 3], k=3))
