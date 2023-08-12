import copy

N = int(input())

lines = []

for n in range(N):
    lines.append(list(input()))

OLD = copy.deepcopy(lines)

for n in range(N):
    for m in range(N):
        if n == 0:
            if m == 0:
                lines[n][m] = OLD[n + 1][m]
            else:
                lines[n][m] = OLD[n][m - 1]
        elif n == N - 1:
            if m == N - 1:
                lines[n][m] = OLD[n - 1][m]
            else:
                lines[n][m] = OLD[n][m + 1]
        else:
            if m == 0:
                lines[n][m] = OLD[n + 1][m]
            elif m == N - 1:
                lines[n][m] = OLD[n - 1][m]
            else:
                continue
    print("".join(lines[n]))
