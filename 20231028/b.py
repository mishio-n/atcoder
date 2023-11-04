import sys

N = input()
a,b,c = map(int,N)

while True:
    ab = a * b
    if ab == c:
        print(f'{a}{b}{c}')
        sys.exit()
    
    if ab >= 10:
        print(f'{a + 1}00')
        sys.exit()
    
    if ab > c:
        print(f'{a}{b}{ab}')
        sys.exit()
    if ab < c:
        b += 1
        c = 0
