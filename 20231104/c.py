import sys

LINES = []

for i in range(9):
    line = input().split()
    if len(set(line)) != 9:
        print("No")
        sys.exit()
    LINES.append(line)
    if i % 3 == 2:
        for j in range(3):
            if len(set([
                  LINES[i - 2][j*3 + 0],
                  LINES[i - 2][j*3 + 1],
                  LINES[i - 2][j*3 + 2],
                  LINES[i - 1][j*3 + 0],
                  LINES[i - 1][j*3 + 1],
                  LINES[i - 1][j*3 + 2],
                  LINES[i][j*3 + 0],
                  LINES[i][j*3 + 1],
                  LINES[i][j*3 + 2],
                ])) != 9:
                print("No")
                sys.exit()

t = [list(x) for x in zip(*LINES)]
for i in range(9):
    if len(set(t[i])) != 9:
        print("No")
        sys.exit()

print("Yes")
