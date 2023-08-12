import re
N,M = map(int,input().split())

data = []

for _ in range(N):
    data.append(input())

for n in range(N):
    if n > N - 9:
        break
    line = data[n]
    for matched in re.finditer("###\.", line):
        start = matched.start()
        if start > M - 9:
            break

        if data[n+1][start:start+4] == "###." and data[n+2][start:start+4] == "###." and data[n+3][start:start+4] == "....":
            if data[n+5][start+5:start+9] == "...." and data[n+6][start+5:start+9] == ".###" and data[n+7][start+5:start+9] == ".###" and data[n+8][start+5:start+9] == ".###":
                print(n+1, start+1)

