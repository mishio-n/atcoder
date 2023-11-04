import re

N = int(input())
S = input()

if re.match(r'.*ab.*',S) or re.match(r'.*ba.*',S):
    print("Yes")
else:
    print("No")
