N = int(input())
A = list(map(int, input().split()))

waitDict = {}
result = []

for i, a in enumerate(A):
    if i == 0:
        if a == -1:
            result.append(i+1)
        else:
            waitDict[a] = i+1
        continue

    if a == -1:
        result.append(i+1)
    elif len(result) > 0 and result[-1] == a:
        result.append(i+1)
    else:
        waitDict[a] = i+1
        continue

    while result[-1] in waitDict:
        result.append(waitDict[result[-1]])

print(" ".join(map(str,result)))