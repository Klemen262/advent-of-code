from input15 import data

def merge(intervals):
    if (len(intervals)) == 0:
        return intervals, 0
    s = sorted(intervals)
    new = []
    a = s[0][0]
    b = s[0][1]
    size = 0
    for i in range(1, len(s)):
        if s[i][0] > b + 1:
            new.append((a, b))
            size += b - a
            a = s[i][0]
            b = s[i][1]
        else:
            b = max(s[i][1], b)
    new.append((a, b))
    size += b - a
    return new, size

lines = [line for line in data.split("\n")]

sensors = []
beacons = []
distances = []
for i in range(len(lines)):
    line = lines[i].split(" ")
    sensors.append([int(line[2][2:-1]), int(line[3][2:-1])])
    beacons.append([int(line[8][2:-1]), int(line[9][2:])])
    distances.append(abs(sensors[i][0] - beacons[i][0]) + abs(sensors[i][1] - beacons[i][1]))

intervals = []
for i in range(len(lines)):
    a = distances[i] - abs(sensors[i][1] - 2000000)
    if a > 0:
        intervals.append((sensors[i][0] - a, sensors[i][0] + a))
print(merge(intervals)[1])

for i in range(4000000):
    intervals = []
    for j in range(len(lines)):
        a = distances[j] - abs(sensors[j][1] - i)
        if a > 0:
            intervals.append((sensors[j][0] - a, sensors[j][0] + a))
    if len(merge(intervals)[0]) > 1:
        x = merge(intervals)[0][0][1] + 1
        #print(x, i)
        print(x * 4000000 + i)
