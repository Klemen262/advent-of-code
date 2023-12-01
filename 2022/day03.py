from input03 import data

lines = data.split("\n")

sum = 0
for line in lines:
    size = len(line) //2
    first = set(line[:size])
    second = set(line[size:])
    a = ord(first.intersection(second).pop())
    if (a >= ord('a') and a <= ord('z')):
        sum += a - ord('a') + 1
    elif (a >= ord('A') and a <= ord('Z')):
        sum += a - ord('A') + 1 + 26
print(sum)

sum = 0
for i in range(100):
    elf1 = set(lines[3 * i])
    elf2 = set(lines[3 * i + 1])
    elf3 = set(lines[3 * i + 2])
    a = ord(elf1.intersection(elf2).intersection(elf3).pop())
    if (a >= ord('a') and a <= ord('z')):
        sum += a - ord('a') + 1
    elif (a >= ord('A') and a <= ord('Z')):
        sum += a - ord('A') + 1 + 26
print(sum)
