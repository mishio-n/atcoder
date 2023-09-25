import sys

N,X = map(int, input().split())
scores = list(map(int, input().split()))

sortedScore = sorted(scores)

trimed = sortedScore[1:N-2]

ans = []

if N == 3:
    a, b = sortedScore    
    if a >= X:
        print(0)
        sys.exit()
    if b >= X:
        print(b)
        sys.exit()

    if a < X < b:
        print(X)
        sys.exit()

    print(-1)
    sys.exit()

diff = X - sum(trimed) 
if 0 <= diff <= 100:
    ans.append(diff)

trimed = sortedScore[1:N-1]
if X <= sum(trimed):
    ans.append(sortedScore[-1])

trimed = sortedScore[0:N-2]
if X <= sum(trimed):
    ans.append(0)

if len(ans) == 0:
    print(-1)
    sys.exit()

print(min(ans))
