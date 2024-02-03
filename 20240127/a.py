import re

S = input()

matched = re.match(r'^[A-Z][a-z]*$', S)

if matched:
    print('Yes')
else:
    print('No')