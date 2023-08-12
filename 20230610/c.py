import re, sys

h,w = map(int, input().split())

span = None
startH = None

if w == 2:
    for i in range(h):
        line = input()
        dot = line.find(".")
        if dot != -1:
            print(f"{i + 1} {dot + 1}")
            sys.exit(0)

for i in range(h):
    line = input()
    matched = [m.span() for m in re.finditer(r'#+', line)]
    if len(matched) == 0:
        continue
    
    if len(matched) > 1:
        print(f"{i + 1} {matched[1][0]}")
        sys.exit(0)
    
    nowSpan = matched[0]
    if span == None:
        span = nowSpan
        startH = i
        continue
    
    if span != nowSpan:
        if nowSpan[0] < span[0]:
            print(f"{startH + 1} {span[0]}")
            sys.exit(0)
        elif nowSpan[0] > span[0]:
            print(f"{i + 1} {nowSpan[0]}")
            sys.exit(0)
        elif nowSpan[1] > span[1]:
            print(f"{startH + 1} {nowSpan[1]}")
            sys.exit(0)
        elif nowSpan[1] < span[1]:
            print(f"{i + 1} {span[1]}")
            sys.exit(0)
