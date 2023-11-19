N,M = map(int,input().split())
A = list(map(int,input().split()))

postedDict = {}
postedSet = {}

for i, a in enumerate(A):
    if i == 0:
        postedSet[1] = set()

    if a not in postedDict:
        postedDict[a] = 1
    else:
        postedSet[postedDict[a]].remove(a)
        postedDict[a] += 1
    
    if postedDict[a] not in postedSet:
        postedSet[postedDict[a]] = set()

    postedSet[postedDict[a]].add(a)

    maxValue = max(postedDict.values())
    print(min(postedSet.get(maxValue)))
