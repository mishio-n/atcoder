import re

N = int(input())
S = str(input())

matched = re.search(r'ABC', S)

if matched is None:
    print(-1)
else:
    print(matched.start() + 1)
