from input10 import data
import numpy as np

lines = [line for line in data.split("\n")]

xs = np.zeros(240, dtype=np.int32)
clock = 0
x = 1
for line in lines:
    if line[0] == "n":
        xs[clock] = x
        clock += 1
    else:
        xs[clock] = x
        xs[clock + 1] = x
        x += int(line[5:])
        clock += 2

sum = 0
for i in range(221):
    if i == 20 or i == 60 or i == 100 or i == 140 or i == 180 or i == 220:
        sum += xs[i - 1] * (i)
print(sum)

display = ["", "", "", "", "", ""]
for i in range(6):
    for j in range(40):
        sprite = xs[i * 40 + j]
        display[i] += "##" if abs(sprite - (j)) <= 1 else "  "
    print(display[i])
