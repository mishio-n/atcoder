import sys

M = int(input())
S1 = input()
S2 = input()
S3 = input()

set1 = set(S1)
set2 = set(S2)
set3 = set(S3)

list1 = list(S1 + S1 + S1)
list2 = list(S2 + S2 + S2)
list3 = list(S3 + S3 + S3)

zipped = zip(list1, list2, list3)
all = set1 & set2 & set3

if all == set():
    print(-1)
    sys.exit()

counter = {}
slotNumber = -1

for i in all:
    counter[i] = []

for i, (l1,l2,l3) in enumerate(zipped):
    flg1 = True
    flg2 = True
    flg3 = True

    if l1 in all:
        for c in counter[l1]:
            if [1] == c["line"]:
                flg1 = False
        if flg1 == True:
            counter[l1].append({"line": [1], "sec": i})
            if len(counter[l1]) == 3:
                slotNumber = l1
                break

    if l2 in all:
        for c in counter[l2]:
            if [2] ==  c["line"]:
                flg2 = False
        if flg2 == True:
            if flg1 == True and l2 == l1:
                counter[l1][-1] = {"line": [1,2], "sec": i}
            else:
                counter[l2].append({"line": [2], "sec": i})
            if len(counter[l2]) == 3:
                slotNumber = l2
                break

    if l3 in all:
        for c in counter[l3]:
            if [3] == c["line"]:
                flg3 = False
        if flg3 == True:
            if flg1 == True and flg2 == True and l3 == l1 and l3 == l2:
                counter[l1][-1] = {"line": [1,2,3], "sec": i}
            elif flg1 == True and l3 == l1:
                counter[l1][-1] = {"line": [1,3], "sec": i}
            elif flg2 == True and l3 == l2:
                counter[l2][-1] = {"line": [2,3], "sec": i}
            else:
                counter[l3].append({"line": [3], "sec": i})

        if len(counter[l3]) == 3:
            slotNumber = l3
            break

print(counter[str(slotNumber)][-1]["sec"])
