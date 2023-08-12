import sys, itertools

N,D = map(int, input().split())

dates = ["o" for _ in range(D)]

for n in range(N):
    s = input()
    x = [i for i, x in enumerate(s) if x == "x"]
    for i in x:
        dates[i] = "x"

try:
  dates.index("o")
except ValueError:
  print(0)
  sys.exit()

print(max(list(map(lambda i: len(list(i[1])), filter(lambda x: x[0] == "o", itertools.groupby(dates))))))
