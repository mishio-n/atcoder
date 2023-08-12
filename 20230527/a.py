import sys

n = int(input())
A = input()
B = input()

for a,b in zip(A, B):
    if a == b:
        continue
    elif a == "1" and b == "l":
        continue
    elif a == "l" and b == "1":
        continue
    elif a == "0" and b == "o":
        continue
    elif a == "o" and b == "0":
        continue
    else:
      print("No")
      sys.exit(0)

print("Yes")