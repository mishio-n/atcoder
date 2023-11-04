import sys

X,Y = map(int,input().split())

diff = X - Y

if diff > 0 and diff <= 3:
    print('Yes')
    sys.exit()
elif diff < 0 and diff >= -2:
    print('Yes')
    sys.exit()

print('No')
