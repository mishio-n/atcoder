N = int(input())
X = 0
Y = 0

for _ in range(N):
    x, y = map(int, input().split())
    X += x
    Y += y

if X > Y:
    print("Takahashi")
elif X < Y:
    print("Aoki")
else:
    print("Draw")