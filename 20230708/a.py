import sys

a, b = map(int, input().split(" "))

if a % 3 != 0:
    if b == a+ 1:
        print("Yes")
        sys.exit(0)

print("No")
