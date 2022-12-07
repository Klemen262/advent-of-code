from input02 import data

scores1 = {'A': {'X': 4, 'Y': 8, 'Z': 3}, 'B': {'X': 1, 'Y': 5, 'Z': 9}, 'C': {'X': 7, 'Y': 2, 'Z': 6}}
scores2 = {'A': {'X': 3, 'Y': 4, 'Z': 8}, 'B': {'X': 1, 'Y': 5, 'Z': 9}, 'C': {'X': 2, 'Y': 6, 'Z': 7}}
sum1 = 0
sum2 = 0
for line in data.split("\n"):
    sum1 += scores1[line[0]][line[2]]
    sum2 += scores2[line[0]][line[2]]
print(sum1)
print(sum2)