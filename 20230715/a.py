N, P, Q = map(int, input().split())
Ds = list(map(int, input().split()))

Dmin = min(Ds)

if P <= Dmin + Q:
    print(P)
else:
    print(Dmin + Q)
