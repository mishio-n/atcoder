import sys

x,y,z = map(int, input().split())
chars = list(input())

capitals = []
old = "a"
for char in chars:
    if char == "A":
        flag = True