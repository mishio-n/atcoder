import math
N = int(input())
A = list(map(int, input().split()))

flg = True
average = 0
goukei = sum(A)
if goukei % N != 0:
    if int(str(goukei / N)[0]) < 5:
      average = math.floor(goukei / N)
    else:
      average = math.floor(goukei / N)
    flg = False
else:
    average = goukei / N

positive = []
negative = []
for a in A:
    if a > average:
        positive.append(a - average)
    else:
        negative.append(average - a)
    
if flg == True:
    print(sum(positive))
else:
    print(sum(negative))
