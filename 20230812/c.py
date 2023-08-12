import sys

N,M = map(int, input().split())
S = list(input())
C = list(map(int, input().split()))

if len(set(S)) == 1:
    print("".join(S))
    sys.exit()

if M == 1:
    print("".join(S[N-1:]+S[:N-1]))
    sys.exit()


for m in range(M):
    index = [(i, S[i]) for i, x in enumerate(C) if x == m+1]
    if len(index) == 1:
        continue
    for i, I in enumerate(index):
        s = index[i - 1][1]
        S[I[0]] = s

print("".join(S))
