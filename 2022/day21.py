from input21 import data

monkeys = {}
not_solved = data.split("\n")
while "root" not in monkeys.keys():
    solving = not_solved
    not_solved = []
    for line in solving:
        words = line.split(" ")
        if len(words) == 2:
            monkeys[words[0][:-1]] = int(words[1])
        elif words[1] in monkeys.keys() and words[3] in monkeys.keys():
            if words[2] == "+":
                monkeys[words[0][:-1]] = monkeys[words[1]] + monkeys[words[3]]
            if words[2] == "-":
                monkeys[words[0][:-1]] = monkeys[words[1]] - monkeys[words[3]]
            if words[2] == "*":
                monkeys[words[0][:-1]] = monkeys[words[1]] * monkeys[words[3]]
            if words[2] == "/":
                monkeys[words[0][:-1]] = monkeys[words[1]] // monkeys[words[3]]
        else:
            not_solved.append(line)
    solving = not_solved
print(monkeys["root"])


monkeys = {}
should_be = {}
not_solved = data.split("\n")
while "humn" not in should_be.keys():
    solving = not_solved
    not_solved = []
    for line in solving:
        words = line.split(" ")
        if words[0][:-1] == "humn":
            continue
        elif len(words) == 2:
            monkeys[words[0][:-1]] = int(words[1])
        elif words[0][:-1] == "root":
            if words[1] in monkeys.keys():
                should_be[words[3]] = monkeys[words[1]]
            elif words[3] in monkeys.keys():
                should_be[words[1]] = monkeys[words[3]]
            else:
                not_solved.append(line)
        elif words[1] in monkeys.keys() and words[3] in monkeys.keys():
            if words[2] == "+":
                monkeys[words[0][:-1]] = monkeys[words[1]] + monkeys[words[3]]
            if words[2] == "-":
                monkeys[words[0][:-1]] = monkeys[words[1]] - monkeys[words[3]]
            if words[2] == "*":
                monkeys[words[0][:-1]] = monkeys[words[1]] * monkeys[words[3]]
            if words[2] == "/":
                monkeys[words[0][:-1]] = monkeys[words[1]] // monkeys[words[3]]
        elif words[1] in monkeys.keys() and words[0][:-1] in should_be.keys():
            if words[2] == "+":
                should_be[words[3]] = should_be[words[0][:-1]] - monkeys[words[1]]
            if words[2] == "-":
                should_be[words[3]] = -should_be[words[0][:-1]] + monkeys[words[1]]
            if words[2] == "*":
                should_be[words[3]] = should_be[words[0][:-1]] // monkeys[words[1]]
            if words[2] == "/":
                should_be[words[3]] = monkeys[words[1]] // should_be[words[0][:-1]]
        elif words[3] in monkeys.keys() and words[0][:-1] in should_be.keys():
            if words[2] == "+":
                should_be[words[1]] = should_be[words[0][:-1]] - monkeys[words[3]]
            if words[2] == "-":
                should_be[words[1]] = should_be[words[0][:-1]] + monkeys[words[3]]
            if words[2] == "*":
                should_be[words[1]] = should_be[words[0][:-1]] // monkeys[words[3]]
            if words[2] == "/":
                should_be[words[1]] = should_be[words[0][:-1]] * monkeys[words[3]]
        else:
            not_solved.append(line)
    solving = not_solved
print(should_be["humn"])