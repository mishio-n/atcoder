import sys

N = int(input())

KYOTEN = []

for i in range(N):
    KYOTEN.append(list(map(int,input().split())))

sorted_KYOTEN = sorted(KYOTEN, key=lambda x: x[0], reverse=True)

top = sorted_KYOTEN.pop(0)

if top[1] < 9:
    diff = 9 - top[1]
    can_join = list(filter(lambda x: (x[1] + diff) % 24 >= 9 and (x[1] + diff) % 24 <= 18 , sorted_KYOTEN))
    total = sum(i[0] for i in can_join) + top[0]
    print(total)
    sys.exit()

elif top[1] > 17:
    diff = top[1] - 17
    can_join = list(filter(lambda x: (x[1] - diff) % 24 >= 9 and (x[1] - diff) % 24 <= 18 , sorted_KYOTEN))
    total = sum(i[0] for i in can_join) + top[0]
    print(total)
    sys.exit()
