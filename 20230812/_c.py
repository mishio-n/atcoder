import copy

N,M = map(int, input().split())
S = list(input())
C = list(map(int, input().split()))
T = copy.deepcopy(S)

P = []
for _ in range(M):
    P.append([])

for i, s in enumerate(S):
    P[C[i]-1].append(i)

for m in range(M):
    for i, p in enumerate(P[m]):
        T[p] = S[P[m][i-1]]

print("".join(T))
