from input09 import data
import numpy as np

lines = [line for line in data.split("\n")]

dir1 = {"U": -1, "D": 1, "L": 0, "R": 0}
dir2 = {"U": 0, "D": 0, "L": -1, "R": 1}

visited = np.zeros((10000,10000), dtype=bool)
h1 = h2 = t1 = t2 = 5000

for line in lines:
    dir, nn = line.split(" ")
    n = int(nn)
    #print(dir, n)
    for _ in range(n):
        h1 += dir1[dir]
        h2 += dir2[dir]

        # follow along line
        if h1 == t1 and abs(h2 - t2) == 2:
            t2 = (h2 + t2) // 2
        elif h2 == t2 and abs(h1 - t1) == 2:
            t1 = (h1 + t1) // 2
        
        # diagonal follow
        elif abs(h1 - t1) == 1 and abs(h2 - t2) == 2:
            t1 = h1
            t2 = (h2 + t2) // 2
        elif abs(h2 - t2) == 1 and abs(h1 - t1) == 2:
            t2 = h2
            t1 = (h1 + t1) // 2
        
        visited[t1, t2] = True
    #print(np.array(visited[4995:5005, 4995:5005], dtype=np.int32))
print(np.sum(visited))


d1 = np.zeros(10, dtype=np.int32)
d2 = np.zeros(10, dtype=np.int32)
d1[:] = 5000
d2[:] = 5000
visited = np.zeros((10000,10000), dtype=bool)

for line in lines:
    dir, nn = line.split(" ")
    n = int(nn)
    #print(dir, n)
    for _ in range(n):
        d1[0] += dir1[dir]
        d2[0] += dir2[dir]
        for i in range(9):
            # follow along line
            if d1[i] == d1[i + 1] and abs(d2[i] - d2[i + 1]) == 2:
                d2[i + 1] = (d2[i] + d2[i + 1]) // 2
            elif d2[i] == d2[i + 1] and abs(d1[i] - d1[i + 1]) == 2:
                d1[i + 1] = (d1[i] + d1[i + 1]) // 2
            
            # diagonal follow
            elif abs(d1[i] - d1[i + 1]) == 1 and abs(d2[i] - d2[i + 1]) == 2:
                d1[i + 1] = d1[i]
                d2[i + 1] = (d2[i] + d2[i + 1]) // 2
            elif abs(d2[i] - d2[i + 1]) == 1 and abs(d1[i] - d1[i + 1]) == 2:
                d2[i + 1] = d2[i]
                d1[i + 1] = (d1[i] + d1[i + 1]) // 2
            
            # diagonal follow 2
            elif abs(d1[i] - d1[i + 1]) == 2 and abs(d2[i] - d2[i + 1]) == 2:
                d1[i + 1] = (d1[i] + d1[i + 1]) // 2
                d2[i + 1] = (d2[i] + d2[i + 1]) // 2
            
        visited[d1[9], d2[9]] = True
        #print(dir)
        #print(d1)
        #print(d2)
        #visited1 = np.zeros((10000,10000), dtype=np.int32)
        #visited1[d1,d2] = np.arange(10)
        #print(np.array(visited1[4985:5015,4985:5015], dtype=np.int32))
    #print(d1)
    #print(d2)
print(np.sum(visited))