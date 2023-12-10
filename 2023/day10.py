import numpy as np

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]

    a = {".": 0, "|": 1, "-": 2, "L": 3, "J": 4, "7": 5, "F": 6, "S": 7}
    l = []
    for line in lines:
        l.append([a[char] for char in line])
    m = np.array(l)
    west = (m == 2) + (m == 4) + (m == 5) + (m == 7)
    north = (m == 1) + (m == 3) + (m == 4) + (m == 7)
    east = (m == 2) + (m == 3) + (m == 6) + (m == 7)
    south = (m == 1) + (m == 5) + (m == 6) + (m == 7)

    n = np.zeros_like(m) - 1
    n[m == 7] = 0
    i = 0
    while (n == i).sum() > 0:
        n[:,:-1][(n[:,1:] == i) * (n[:,:-1] == -1) * (west[:,1:]) * (east[:,:-1])] = i + 1
        n[:,1:][(n[:,:-1] == i) * (n[:,1:] == -1) * (west[:,1:]) * (east[:,:-1])] = i + 1
        n[:-1,:][(n[1:,:] == i) * (n[:-1,:] == -1) * (north[1:,:]) * (south[:-1,:])] = i + 1
        n[1:,:][(n[:-1,:] == i) * (n[1:,:] == -1) * (north[1:,:]) * (south[:-1,:])] = i + 1
        i = i+1
    return n.max()

def puzzle2(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]

    a = {".": 0, "|": 1, "-": 2, "L": 3, "J": 4, "7": 5, "F": 6, "S": 7}
    l = []
    for line in lines:
        l.append([a[char] for char in line])
    m = np.array(l)
    west = (m == 2) + (m == 4) + (m == 5) + (m == 7)
    north = (m == 1) + (m == 3) + (m == 4) + (m == 7)
    east = (m == 2) + (m == 3) + (m == 6) + (m == 7)
    south = (m == 1) + (m == 5) + (m == 6) + (m == 7)

    n = np.zeros_like(m) - 1
    n[m == 7] = 0
    i = 0
    while (n == i).sum() > 0:
        n[:,:-1][(n[:,1:] == i) * (n[:,:-1] == -1) * (west[:,1:]) * (east[:,:-1])] = i + 1
        n[:,1:][(n[:,:-1] == i) * (n[:,1:] == -1) * (west[:,1:]) * (east[:,:-1])] = i + 1
        n[:-1,:][(n[1:,:] == i) * (n[:-1,:] == -1) * (north[1:,:]) * (south[:-1,:])] = i + 1
        n[1:,:][(n[:-1,:] == i) * (n[1:,:] == -1) * (north[1:,:]) * (south[:-1,:])] = i + 1
        i = i+1
    
    result = 0
    for l in range(len(lines)):

        # !!!! hardcoded from my example
        line = lines[l].replace("S", "|")

        for i in range(len(line)):
            if n[l,i] == -1:
                outside = True
                up = False
                down = False
                for j in range(i):
                    c = line[j]
                    if n[l,j] != -1 and c == "|":
                        outside = not outside
                    if n[l,j] != -1 and c == "L":
                        up = True
                    if n[l,j] != -1 and c == "F":
                        down = True
                    if n[l,j] != -1 and c == "7" and up:
                        up = False
                        outside = not outside
                    if n[l,j] != -1 and c == "7" and down:
                        down = False
                    if n[l,j] != -1 and c == "J" and up:
                        up = False
                    if n[l,j] != -1 and c == "J" and down:
                        down = False
                        outside = not outside
                if not outside:
                    result += 1
    
    return result

def main():

    input_file = open("input10.txt")
    input = input_file.read()

    test_input_1 = """.....
.S-7.
.|.|.
.L-J.
.....
"""

    test_input_2 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""
    #test_input_2 = test_input_1

    test_result_1 = 4
    test_result_2 = 10

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
