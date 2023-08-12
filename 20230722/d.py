N, M = map(int, input().split())

lines = []

first_iwa_yoko = N -1
first_iwa_tate = M -1

for n in range(N):
    line = list(input())
    lines.append(line)
    if n == 0:
        continue
    if n == N-1:
        continue
    if n == 1:
        iwa = line[1:].index("#")
        if iwa != M-2:
            first_iwa_yoko = iwa
    
    if line[1] == "#":
        if first_iwa_tate == M -1:
            first_iwa_tate = n

print(first_iwa_yoko, first_iwa_tate)
