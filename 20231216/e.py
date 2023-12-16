import sys

N = int(input())

potionSet = set()
maxPostionNum = 0
actionList = []
enemyList = []
inputs = []

for n in range(N):
    event, type = input().split()
    inputs.append(f'{event} {type}')
    if event == "2":
        enemyList.append(type)

for n in range(N):
    event, type = inputs[n].split()
    if event == "1":
        if type in potionSet:
            actionList.append("0")
        elif type not in enemyList:
            actionList.append("0")
        else:
            potionSet.add(type)
            actionList.append("1")
            if len(potionSet) > maxPostionNum:
                maxPostionNum = len(potionSet)
    else:
        if type in potionSet:
            potionSet.remove(type)
            enemyList.pop(0)
        else:
            print(-1)
            sys.exit()

print(maxPostionNum)
print(" ".join(actionList))