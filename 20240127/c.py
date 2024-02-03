import itertools

N = int(input())

Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_LIST = [[0] * N]
B_LIST = [[0] * N]

x = 0

served_list = []

while True:
    if x > max(Q) + 1:
        break

    y = []
    for n in range(N):
        a = A[n] * x
        if a > Q[n]:
            y.append(0)

        if B[n] != 0:
            y.append((Q[n] - a) // B[n])
    served_list.append(x + min(y))
    
    x += 1

print(max(served_list))