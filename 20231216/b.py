S = input()
T = input()

shorts = ["AE", "AB", "BA", "BC", "CB", "CD", "DC", "DE", "ED", "EA"]
longs = ["AC", "AD", "BD", "BE", "CE", "CA", "DA", "DB", "EC", "EB"]

if S in shorts:
    if T in shorts:
        print("Yes")
    else:
        print("No")
else:
    if T in longs:
        print("Yes")
    else:
        print("No")