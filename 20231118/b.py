N = int(input())
A = list(map(int, input().split()))

setA = set(A)
maxA = max(A)

setA.remove(maxA)

print(max(setA))
