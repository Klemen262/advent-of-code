from input14 import data
import numpy as np

rock = [[(int(pair.split(",")[0]), int(pair.split(",")[1])) for pair in line.split(" -> ")] for line in data.split("\n")]
cave = np.zeros((170, 680), dtype=np.int8)

xs = []
for i in range(len(rock)):
    for j in range(1, len(rock[i])):
        x2 = rock[i][j][1]
        x1 = rock[i][j-1][1]
        y2 = rock[i][j][0]
        y1 = rock[i][j-1][0]
        xs.append(x1)
        xs.append(x2)
        if x1 == x2:
            cave[x1, min(y1, y2) : max(y1, y2) + 1] = 1
        else:
            cave[min(x1, x2) : max(x1, x2) + 1, y1] = 1
#print(min(xs), max(xs))
cave2 = cave.copy()

ended = False
sand = 0
while not ended:
    i, j = 0, 500
    bottom = cave[i + 1, j - 1: j + 2]
    while bottom.sum() < 3:
        i += 1
        if bottom[1] != 0:
            j += -1 if bottom[0] == 0 else 1
        if i >= cave.shape[0] - 1:
            ended = True
            break
        bottom = cave[i + 1, j - 1: j + 2]
    if not ended:
        cave[i, j] = 1
        sand += 1
print(sand)

cave2[max(xs) + 2, :] = 1
cave = cave2

ended = False
sand = 0
while not ended and cave[0, 500] == 0:
    i, j = 0, 500
    bottom = cave[i + 1, j - 1: j + 2]
    while bottom.sum() < 3:
        i += 1
        if bottom[1] != 0:
            j += -1 if bottom[0] == 0 else 1
        if i >= cave.shape[0] - 1:
            ended = True
            break
        bottom = cave[i + 1, j - 1: j + 2]
    if not ended:
        cave[i, j] = 1
        sand += 1
print(sand)
