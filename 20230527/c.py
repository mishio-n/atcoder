import sys

n,m,h,k = map(int, input().split())
s = list(input())
potions = set()
pos = (0,0)
for i in range(m):
    x,y = map(int, input().split())
    potions.add((x,y))

for char in s:
    h -= 1

    if h < 0:
        print("No")
        sys.exit(0)

    if char == "R":
        pos = (pos[0] + 1, pos[1])
    elif char == "L":
        pos = (pos[0] - 1, pos[1])
    elif char == "U":
        pos = (pos[0], pos[1] + 1)
    elif char == "D":
        pos = (pos[0], pos[1] - 1)

    if pos in potions:
        if h < k:
            potions.remove(pos)
            h = k

print("Yes")