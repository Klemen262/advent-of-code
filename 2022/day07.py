from input07 import data

sizes = []
sum = 0
needs = -40000000
for line in data.split("\n"):
    words = line.split(" ")
    if words[0] == "$" and words[1] == "cd" and words[2] == "..":
        if sizes[-1] <= 100000:
            sum += sizes[-1]
        sizes = sizes[:-1]
    elif words[0] == "$" and words[1] == "cd":
        sizes.append(0)
    elif words[0] != "dir" and words[0] != "$":
        size = int(words[0])
        needs += size
        for i in range(len(sizes)):
            sizes[i] += size
print(sum)

sizes = []
smallest = 70000000
for line in data.split("\n"):
    words = line.split(" ")
    if words[0] == "$" and words[1] == "cd" and words[2] == "..":
        if sizes[-1] >= needs and sizes[-1] < smallest:
            smallest = sizes[-1]
        sizes = sizes[:-1]
    elif words[0] == "$" and words[1] == "cd":
        sizes.append(0)
    elif words[0] != "dir" and words[0] != "$":
        size = int(words[0])
        for i in range(len(sizes)):
            sizes[i] += size
print(smallest)