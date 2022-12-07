from input01 import data

sum = 0
max = 0
max2 = 0
max3 = 0
for line in data.split("\n"):
    if line == "":
        if sum > max3:
            max3 = sum
            if sum > max2:
                max3 = max2
                max2 = sum
                if sum > max:
                    max2 = max
                    max = sum
        sum = 0
    else:
        sum += int(line)
print(max)
print(max + max2 + max3)