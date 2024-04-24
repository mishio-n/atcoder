N = int(input())
A = list(map(int, input().split()))

operations = []

for i in range(N):
    if A[i] == i + 1:
        continue

    while True:
        operations.append((i + 1, A[i]))

        targetIndex = A[i] - 1
        targetIndexOld = A[targetIndex]
        A[targetIndex] = A[i]
        A[i] = targetIndexOld

        if A[i] == i + 1:
            break

print(len(operations))

for operation in operations:
    print(*operation)
