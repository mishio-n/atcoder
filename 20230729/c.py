import sys

N, M = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

if min(A) > max(B):
    print(max(B) + 1)
    sys.exit()

if N < M:
  if min(B) > max(A):
      print(max(A))
      sys.exit()
else:
  if min(B) > max(A):
      print(max(B + 1))
      sys.exit()

for m in range(M):
    b = B[m]
    alist = list(filter(lambda a: a <= b, A))
    if len(alist) == M - m:
        print(min(alist))
        sys.exit()
    if len(alist) > M - m:
        print(min(alist))
        sys.exit()

# for n in range(N):
#     a = A[n]
#     B = list(filter(lambda b: b >= a, B))
#     if len(B) <= n + 1:
#         print(a)
#         sys.exit()
