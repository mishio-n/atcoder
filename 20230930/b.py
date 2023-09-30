import re

N, M = map(int, input().split())
S = input()
T = input()

point = 3

if re.search(rf'^{S}', T) is not None:
    point -= 2

if re.search(rf'{S}$', T) is not None:
    point -= 1

print(point)
