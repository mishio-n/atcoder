N = int(input())

better = []
winner = []
winnerBetNum = 0

for n in range(N):
    betNum = int(input())
    target = list(map(int, input().split()))
    better.append((n+1,betNum, target))

X = int(input())

better.sort(key=lambda x: x[1])

for b in better:
    if winnerBetNum != 0 and b[1] > winnerBetNum:
        break
    if X not in b[2]:
        continue
    
    winner.append(b[0])
    winnerBetNum = b[1]

print(len(winner))
print(*winner, sep=" ")
