import itertools

N,T,M = map(int, input().split())

badPairs = [()]

for n in range(M):
    a,b = map(int, input().split())
    badPairs.append((a,b))

members = list(range(1,N+1))

roop = N / 2

for i in
itertools.combinations(members, 2)
