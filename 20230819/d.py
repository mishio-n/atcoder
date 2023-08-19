import copy

H,W = map(int,input().split())

coockies = []

for _ in range(H):
    coockies.append(list(input()))


while True:
    flgH = False
    flgW = False
    for h in range(H):
        setted = set(coockies[h])
        if len(setted) == 1:
            if "." not in setted:
                coockies[h] = ["."] * W
                flgH = True
        elif len(setted) == 2:
            if "." in setted:
                coockies[h] = ["."] * W
                flgH = True

    transposed  = list(map(list, zip(*coockies)))
    for w in range(W):
        setted = set(transposed[w])
        if len(setted) == 1:
            if "." not in setted:
                transposed[w] = ["."] * H
                flgW = True
        elif len(setted) == 2:
            if "." in setted:
                transposed[w] = ["."] * H
                flgW = True
      
    coockies = list(map(list, zip(*transposed)))
      
    if flgH == False and flgW == False:
        break

print(coockies)
