n = int(input())
times = list(map(int, input().split()))
q = int(input())

array = []
for i in range(n):
    if i == 0:
        continue
    array.append(range(times[i-1], times[i]+1))

print(array)

for i in range(q):
    start, end = map(int, input().split())
    targetRange = range(start, end+1)
    for ran in array:
        

rs = [x, y,]
z = (
    i
    for i in range(
        min(e for r in rs for e in (r.start, r.stop)),
        max(e for r in rs for e in (r.start, r.stop))
    )
    if all(i in r for r in rs)
)
