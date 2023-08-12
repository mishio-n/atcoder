n = int(input())

rest = n % 5

if rest == 0:
    print(n)
elif rest <= 2:
    print(n - rest)
else:
    print(n + (5 - rest))
