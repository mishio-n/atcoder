N, M = map(int, input().split())

HANABI = set(map(int, input().split()))
DAY = set(range(1, N + 1))

ans = list('0' * N)
prev = None

no_hanabi_days = sorted(list(HANABI.symmetric_difference(DAY)), reverse=True)

for i, hanabi in enumerate(no_hanabi_days):
    if prev is None:
        ans[hanabi -1] = str(1)
        prev = hanabi + 1
        continue

    if no_hanabi_days[i - 1] - hanabi == 1:
        ans[hanabi -1] = str(prev - hanabi)
    else:
        ans[hanabi -1] = str(1)
        prev = hanabi + 1

print('\n'.join(ans))
