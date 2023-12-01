from input11 import data

lines = [line for line in data.split("\n")]

monkeys = []
activness = []
for i in range((len(lines) + 1) // 7):
    monkeys.append([int(a) for a in lines[i * 7 + 1][18:].split(", ")])
    activness.append(0)


for _ in range(20):
    for i in range((len(lines) + 1) // 7):
        activness[i] += len(monkeys[i])
        for item in monkeys[i]:
            old = item
            old = eval(lines[i * 7 + 2][19:]) // 3
            if old % int(lines[i * 7 + 3][21:]) == 0:
                monkeys[int(lines[i * 7 + 4][29:])].append(old)
            else:
                monkeys[int(lines[i * 7 + 5][30:])].append(old)
        monkeys[i] = []

print(sorted(activness)[-1] * sorted(activness)[-2])


monkeys = []
activness = []
lcm = 1
for i in range((len(lines) + 1) // 7):
    lcm *= int(lines[i * 7 + 3][21:])
    monkeys.append([int(a) for a in lines[i * 7 + 1][18:].split(", ")])
    activness.append(0)

for _ in range(10000):
    for i in range((len(lines) + 1) // 7):
        activness[i] += len(monkeys[i])
        for item in monkeys[i]:
            old = item
            old = eval(lines[i * 7 + 2][19:]) % lcm
            if old % int(lines[i * 7 + 3][21:]) == 0:
                monkeys[int(lines[i * 7 + 4][29:])].append(old)
            else:
                monkeys[int(lines[i * 7 + 5][30:])].append(old)
        monkeys[i] = []

print(sorted(activness)[-1] * sorted(activness)[-2])