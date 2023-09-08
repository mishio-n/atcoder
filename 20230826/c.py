N,M = map(int,input().split())
G = [[] for _ in range(N)]
d = [0]*N

for i in range(M):
    x, y, z = map(int, input().split())
    G[x-1].append(y-1)
    G[y-1].append(x-1)
    d[x-1] += 1
    d[y-1] += 1

checklist = []
length = 0
for i in range(len(d)):
    if d[i]==0:
        checklist.append(i)

print(d)
print(checklist)

while len(checklist)>0:
    nextlist = []
    for i in checklist:
        for j in G[i]:
            d[j] -= 1
            if d[j] == 0:
                nextlist.append(j)
    checklist = nextlist.copy()
    length += 1 

print(length-1)
