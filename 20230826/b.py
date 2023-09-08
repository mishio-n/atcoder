import sys

N = int(input())
A = list(map(int,input().split()))

A.sort()

for i, a in enumerate(A):
    if i == 0:
        continue
    
    if a != A[i-1] + 1:
        print(a - 1)
        sys.exit()
