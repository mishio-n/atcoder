import sys

N, M = map(int, input().split())

top = set()
other = set()

for m in range(M):
    info = list(map(int, input().split()))
    if m == 0:
        top.add(info[0])
        other.add(info[1])
        continue
    
    if (info[0] in top) and (info[1] in top):
        top.discard(info[1])
        other.add(info[1])
        continue
    
    if info[0] in other and info[1] in top:
        top.discard(info[1])
        other.add(info[1])
        continue

    if info[0] in other:
        other.add(info[1])
        continue

    if info[1] in top:
        top.discard(info[1])
        other.add(info[1])
        top.add(info[0])
        continue

    top.add(info[0])
    other.add(info[1])


if len(top) != 1:
    print(-1)
    sys.exit()

print(top.pop())
