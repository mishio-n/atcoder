H, W, N = map(int, input().split())

DIRECTION = "UP"
POSITION = (0, 0)

def turn(direction, reverse=False):
    if direction == "UP":
        if reverse:
            return "LEFT"
        else:
            return "RIGHT"
    if direction == "RIGHT":
        if reverse:
            return "UP"
        else:
            return "DOWN"
    if direction == "DOWN":
        if reverse:
            return "RIGHT"
        else:
            return "LEFT"
    if direction == "LEFT":
        if reverse:
            return "DOWN"
        else:
            return "UP"

area = [["." for _ in range(W)] for _ in range(H)]

for _ in range(N):
    x, y = POSITION

    if area[y][x] == ".":
        area[y][x] = "#"
        DIRECTION = turn(DIRECTION)
    else:
        area[y][x] = "."
        DIRECTION = turn(DIRECTION, reverse=True)

    if DIRECTION == "UP":
        y -= 1
        if y < 0:
            y = H - 1
    if DIRECTION == "RIGHT":
        x += 1
        if x == W:
            x = 0
    if DIRECTION == "DOWN":
        y += 1
        if y == H:
            y = 0
    if DIRECTION == "LEFT":
        x -= 1
        if x < 0:
            x = W - 1

    POSITION = (x, y)

for row in area:
    print("".join(row))