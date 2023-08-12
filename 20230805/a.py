import sys
N = int(input())

if N == 1:
    print(0)
    sys.exit()

P = list(map(int, input().split()))

P1 = P.pop(0)
rest = set(P)
maxP = max(P)


if P1 > maxP:
    print(0)
    sys.exit()

if P1 == maxP:
    print(1)
    sys.exit()

print(maxP - P1 + 1)
