import sys

n,m,h,k = map(int, input().split())
s = list(input())
potions = []
pos = [0,0]
for i in range(m):
    x,y = map(int, input().split())
    potions.append([x,y])


def move(char, pos):
    if char == "R":
        pos[0] += 1
    elif char == "L":
        pos[0] -= 1
    elif char == "U":
        pos[1] += 1
    elif char == "D":
        pos[1] -= 1
    return pos

for char in s:
    h -= 1

    if h < 0:
        print("No")
        sys.exit(0)

    pos = move(char, pos)
    if pos in potions:
        if h < k:
            potions.remove(pos)
            h = k

print("Yes")