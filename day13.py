from input13 import data

pairs = [pair for pair in data.split("\n\n")]

def compare(a, b):
    if type(a) == list and type(b) == list:
        for i in range(min(len(a), len(b))):
            diff = compare(a[i], b[i])
            if diff != 0:
                return diff
        return len(a) - len(b)
    elif type(a) == int and type(b) == int:
        return a - b
    elif type(a) == list:
        return compare(a, [b])
    else:
        return compare([a], b)

sum = 0
packets = [[[2]], [[6]]]
for i in range(len(pairs)):
    a, b = [eval(x) for x in pairs[i].split("\n")]
    packets.append(a)
    packets.append(b)
    if compare(a, b) < 0:
        sum += i + 1
print(sum)

ordered = []
while packets != []:
    new_packets = []
    smallest = None
    for pack in packets:
        if smallest == None:
            smallest = pack
        elif compare(pack, smallest) < 0:
            new_packets.append(smallest)
            smallest = pack
        else:
            new_packets.append(pack)
    ordered.append(smallest)
    packets = new_packets
    new_packets = []

i = ordered.index([[2]]) + 1
j = ordered.index([[6]]) + 1
print(i * j)