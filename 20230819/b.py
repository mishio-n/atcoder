import sys

M = int(input())
D = list(map(int,input().split()))

total = sum(D)
middleDay = int((total + 1) / 2)

tmp = 0

if M == 1:
    print(1, middleDay)
    sys.exit()

for i, d in enumerate(D):
    tmp = tmp + d

    if tmp >= middleDay:
        tmp = tmp - d
        diff = middleDay - tmp
        print(i + 1, diff)
        break
