def solve(s, k):
    start, ans = 0, 0
    unique = ''
    for i in range(len(s)):
        unique = unique + s[i]
        while len(set(unique)) > k:
            unique = unique[start+1:]
            start = start + 1
        if len(set(unique)) == k:
            ans = max(i - start + 1, ans)
    print(ans)


if __name__ == '__main__':
    solve(s='aabacebebebe', k=3)
