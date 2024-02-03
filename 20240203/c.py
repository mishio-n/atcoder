N = int(input())
A = list(map(int, input().split()))

passenger = 0

for i in range(N):
    if A[i] > 0:
        passenger += A[i]
    else:
        if passenger < abs(A[i]):
            passenger = 0
        else:
            passenger -= abs(A[i])

print(passenger)