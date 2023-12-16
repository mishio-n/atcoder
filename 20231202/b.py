n = 3
w = [6, 8, 12]
v = [600, 800, 1200]

W = 99

dp = [[0] * (W + 1) for i in range(n + 1)]

exceeded = False

for i in range(n):
    for j in range(W + 1):
        if j < w[i] or exceeded == False:
            dp[i + 1][j] = dp[i][j]
            if not j < w[i]:
                exceeded = True
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - w[i]] + v[i])

print(dp[n][W])
