from input05 import stacks_input, moves

stacks1 = [[] for _ in range(9)]
stacks2 = [[] for _ in range(9)]
for line in stacks_input.split("\n")[::-1]:
    for i in range(9):
        char = line[4 * i + 1]
        if char != ' ':
            stacks1[i].append(char)
            stacks2[i].append(char)

for line in moves.split("\n"):
    n, fr, to = [int(a) for a in line.split(" ")[1::2]]
    fr -= 1
    to -= 1
    for i in range(n):
        stacks1[to].append(stacks1[fr][-1])
        stacks1[fr] = stacks1[fr][:-1]
    stacks2[to] += stacks2[fr][-n:]
    stacks2[fr] = stacks2[fr][:-n]
print("".join([a[-1] for a in stacks1]))
print("".join([a[-1] for a in stacks2]))