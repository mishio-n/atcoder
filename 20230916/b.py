import sys

S = str(input())

kaibun = set()

if len(set(S)) == 1:
    print(len(S))
    sys.exit()

if len(set(S)) == len(S):
    print(1)
    sys.exit()

for i in range(len(S)):
    low, high = i, i
    while low >= 0 and high < len(S) and S[low] == S[high]:
        kaibun.add(S[low:high+1])
        low -= 1
        high += 1

for i in range(len(S)):
    low, high = i, i+1
    while low >= 0 and high < len(S) and S[low] == S[high]:
        kaibun.add(S[low:high+1])
        low -= 1
        high += 1

print(len(max(kaibun, key=len)))
