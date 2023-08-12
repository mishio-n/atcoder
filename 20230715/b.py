import itertools, sys

N, M = map(int, input().split())

products = []
for n in range(N):
    products.append(list(map(int, input().split())))

permutations = list(itertools.permutations(products, 2))

for pair in permutations:
    functionsI = set(pair[0][2:])
    functionsJ = set(pair[1][2:])

    if pair[0][0] < pair[1][0]:
        continue
    
    if pair[0][0] == pair[1][0]:
        # 価格が同じ場合は、I機能がJ機能の真部分集合である
        if functionsI < functionsJ:
            print("Yes")
            sys.exit(0)
        else:
            continue

    if functionsI <= functionsJ:
        print("Yes")
        sys.exit(0)

print("No")
