N = int(input())

result = set()
reverResult = set()

for i in range(N):
    flg = True
    s = input()
    if s == "":
        break
    if i == 0:
        result.add(s)
        reverResult.add(s[::-1])
        continue
    if s in result:
        continue
    if s in reverResult:
        continue

    result.add(s)
    reverResult.add(s[::-1])

print(len(result))
