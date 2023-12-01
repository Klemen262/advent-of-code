from input08 import data
import numpy as np

sum = 0
a = np.array([[int(tree) for tree in line] for line in data.split("\n")])
visible = 0
for i in range(1, a.shape[0] - 1):
    for j in range(1, a.shape[1] - 1):
        if np.max(a[i,:j]) < a[i,j] or np.max(a[i,j+1:]) < a[i,j] or np.max(a[:i,j]) < a[i,j] or np.max(a[i+1:,j]) < a[i,j]:
            visible += 1
print(visible + 2 * a.shape[0] + 2 * a.shape[1] - 4)

maxScore = 0
for i in range(1, a.shape[0] - 1):
    for j in range(1, a.shape[1] - 1):
        score = 1

        x = i + 1
        y = j
        part_score = 0
        while x >= 0 and y >= 0 and x < a.shape[0] and y < a.shape[1]:
            part_score += 1
            if a[x, y] >= a[i, j]:
                break
            x += 1
        score *= part_score

        x = i - 1
        y = j
        part_score = 0
        while x >= 0 and y >= 0 and x < a.shape[0] and y < a.shape[1]:
            part_score += 1
            if a[x, y] >= a[i, j]:
                break
            x -= 1
        score *= part_score

        x = i
        y = j + 1
        part_score = 0
        while x >= 0 and y >= 0 and x < a.shape[0] and y < a.shape[1]:
            part_score += 1
            if a[x, y] >= a[i, j]:
                break
            y += 1
        score *= part_score

        x = i
        y = j - 1
        part_score = 0
        while x >= 0 and y >= 0 and x < a.shape[0] and y < a.shape[1]:
            part_score += 1
            if a[x, y] >= a[i, j]:
                break
            y -= 1
        score *= part_score

        maxScore = max(maxScore, score)
print(maxScore)