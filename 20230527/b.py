import itertools, sys

n, m = map(int, input().split())

l = list(range(1,n+1))
pairs = list(itertools.combinations(l, 2))
# print(pairs)

for i in range(m):
    line = list(map(int, input().split()))
    combinations = list(zip(line,line[1:]))
    for combi in combinations:
        if combi[0] > combi[1]:
            combi = (combi[1], combi[0])
        if combi in pairs:
            pairs.remove(combi)
        
        if len(pairs) == 0:
            print(0)
            sys.exit(0)


print(len(pairs))
