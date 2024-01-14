import re

N = int(input())

binary = bin(N)

matched = re.search(r'0+$', binary)

if matched:
    print(len(matched.group(0)))
else:
    print(0)