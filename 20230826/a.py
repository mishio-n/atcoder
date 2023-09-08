import sys

N,H,X = map(int,input().split())

P = list(map(int,input().split()))

diff = X - H

for n in range(N):
    if P[n] >= diff:
        print(n + 1)
        sys.exit()
