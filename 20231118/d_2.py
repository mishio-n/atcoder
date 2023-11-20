N,M = map(int,input().split())
A = list(map(int,input().split()))

counts = [0] * (N+1)

nowWinner = 1
maxVotes = 0

for i, a in enumerate(A):
    counts[a] += 1

    nowCount = counts[a]
    if nowCount > maxVotes or nowCount == maxVotes and a < nowWinner:
        nowWinner = a
        maxVotes = nowCount

    print(nowWinner)
