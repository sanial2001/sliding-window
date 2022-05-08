def solve(nums, k):
    neg, res = [], []
    for i in range(k):
        if nums[i] < 0:
            neg.append(nums[i])
    i, j = 0, k
    while j < len(nums):
        if nums[j] < 0:
            neg.append(nums[j])
        res.append(0 if len(neg) == 0 else neg[0])
        if len(neg) > 0:
            if nums[i] == neg[0]:
                neg.pop(0)
        i, j = i + 1, j + 1
    res.append(0 if len(neg) == 0 else neg[0])
    return res


if __name__ == '__main__':
    print(solve(nums=[12, -1, -7, 8, -15, 30, 16, 28], k=3))
