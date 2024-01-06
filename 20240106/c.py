from collections import deque

N, Q = map(int, input().split())

DRAGON = deque([(1, 0)])

movedCount = 0

for i in range(Q):
    query, value = input().split()
    if query == '1':
        movedCount += 1
        if value == 'R':
            DRAGON.appendleft((DRAGON[0][0] + 1, DRAGON[0][1]))
        elif value == 'L':
            DRAGON.appendleft((DRAGON[0][0] - 1, DRAGON[0][1]))
        elif value == 'U':
            DRAGON.appendleft((DRAGON[0][0], DRAGON[0][1] + 1))
        elif value == 'D':
            DRAGON.appendleft((DRAGON[0][0], DRAGON[0][1] - 1))
    else:
        value = int(value) - 1
        if value < movedCount:
            print(DRAGON[value][0], DRAGON[value][1])
        else:
            value -= movedCount
            print(value + 1, 0)