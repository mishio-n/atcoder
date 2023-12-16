N = int(input())
A = list(map(int, input().split()))
aDict = {}
dist = []

# 累積和を計算
cumulative_sum = [0] * (N + 1)
for i in range(N):
    cumulative_sum[i + 1] = cumulative_sum[i] + A[i]

for a in A:
    if a in aDict:
        dist.append(str(aDict[a]))
    else:
        aDict[a] = cumulative_sum[0] - (N - a) * a
        dist.append(str(aDict[a]))

print(" ".join(dist))