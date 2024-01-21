import sys, re

H, W, K = map(int, input().split())

lines = []
H_END = False
W_END = False

shortest = 2 * 10**5

for i in range(H):
    lines.append(list(input()))

transed =  [list(x) for x in zip(*lines)]

for i in range(max(H, W)):
    if i < H:
        line = "".join(lines[i])
        matched = re.findall(fr'[.o]{{{K},}}', line)
        for m in matched:
            o_length = m.count('o')
            if K <= o_length:
                print(0)
                sys.exit()
            shortest = K - o_length if shortest > K - o_length else shortest

    if i < W:
        line = "".join(transed[i])
        matched = re.findall(fr'[.o]{{{K},}}', line)
        for m in matched:
            o_length = m.count('o')
            if K <= o_length:
                print(0)
                sys.exit()
            shortest = K - o_length if shortest > K - o_length else shortest

if shortest == 2 * 10**5:
    print(-1)
else:
    print(shortest)