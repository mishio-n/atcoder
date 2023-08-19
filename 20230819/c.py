N = int(input())

ices = []
iceSet = {}
second = None

for _ in range(N):
    f,s = map(int,input().split())
    ices.append((f,s))
    if f in iceSet:
        iceSet[f].add(s)
    else:
        iceSet[f] = set([s])

sortedIces = sorted(ices, key=lambda x: x[1], reverse=True)
top = sortedIces[0]

iceSet[top[0]].remove(top[1])

for ice in sortedIces[1:]:
    if second == None:
        if ice[0] == top[0]:
            second = int(ice[1] / 2)
            continue
        second = ice[1]
        break
    
    if ice[0] == top[0]:
        continue
    else:
        if second < ice[1]:
            second = ice[1]
            break

print(top[1] + second)

