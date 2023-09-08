import sys

N= int(input())

TAKAHASHI_GISEKI = 0
AOKI_GISEKI = 0
TOTAL_GISEKI = 0

SENKYOKU_LIST = []

URAGIRI = 0

for n in range(N):
    X, Y, Z = map(int,input().split())
    if X > Y:
        TAKAHASHI_GISEKI += Z
    else:
        AOKI_GISEKI += Z
    TOTAL_GISEKI += Z
    SENKYOKU_LIST.append([X,Y,Z])

if TAKAHASHI_GISEKI > AOKI_GISEKI:
    print(0)
    sys.exit()

SORTED_SENKYOKU_LIST = sorted(SENKYOKU_LIST, key=lambda x:x[2], reverse=True)

if TAKAHASHI_GISEKI == 0:
    for s in SORTED_SENKYOKU_LIST:
        URAGIRI += int((s[1] - s[0] + 1) / 2)
        TAKAHASHI_GISEKI += s[2]

        if TAKAHASHI_GISEKI >= TOTAL_GISEKI / 2:
            print(URAGIRI)
            sys.exit()

for i, s in enumerate(SORTED_SENKYOKU_LIST):
    diff = (TOTAL_GISEKI / 2) + 1 - TAKAHASHI_GISEKI
    if s[2] < diff:
        URAGIRI += int((s[1] - s[0] + 1) / 2)
        TAKAHASHI_GISEKI += s[2]
        continue

    if s[2] > diff:
        NEXT = SORTED_SENKYOKU_LIST[i+1]
        URAGIRI += int((s[1] - s[0] + 1) / 2)
        if NEXT[2] < diff:
            print(TAKAHASHI_GISEKI + URAGIRI)
            sys.exit()
