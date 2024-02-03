import collections

S = list(input())
s = sorted(S)
counter = collections.Counter(s)
top = max(counter, key=counter.get)
print(top)
