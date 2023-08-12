import sys
N, K = map(int, input().split(" "))

drags = []

for n in range(N):
    drags.append(list(map(int, input().split(" "))))

count = 0

drags.sort(key=lambda x: x[0])

goukei = sum([drags[n][1] for n in range(N)])

if N == 1:
    if drags[0][1] > K:
        print(drags[0][0] + 1)
        sys.exit(0)
    else:
        print(1)
        sys.exit(0)

for n in range(N):
    if K == 0:
        print(drags[-1][0] + 1)
        break
    if count == 0:
        if goukei <= K:
            print(1)
            break
    goukei -= drags[n][1]
    if goukei == K:
        print(drags[n][0] + 1)
        break
    elif goukei < K:
        print(drags[n][0] + 1)
        break
    count += 1
