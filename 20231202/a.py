import sys

M, D = map(int, input().split())
y, m, d = map(int, input().split())

if d != D:
    print(f'{y} {m} {d + 1}')
    sys.exit()

if m != M:
    print(f'{y} {m + 1} 1')
    sys.exit()

print(f'{y + 1} 1 1')