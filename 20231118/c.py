import sys, re

N = int(input())
S = input()

setS = set(S)
findDict = {}

if len(setS) == 1 or len(setS) == N:
    print(N)
    sys.exit()

regexp = re.compile("(.)\\1{%d,}" % 0)
searched = regexp.finditer(S)
mapped = map(lambda x: x.group(), searched)

for m in mapped:
    if m[0] not in findDict:    
        findDict[m[0]] = len(m)
        continue

    if findDict[m[0]] < len(m):
        findDict[m[0]] = len(m)

print(sum(findDict.values()))
