import numpy as np

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    mirrors = np.array([[a for a in line] for line in lines])
    height, width = mirrors.shape
    visited = np.zeros_like(mirrors)
    waiting = [(0, 0, "r")]
    while len(waiting) > 0:
        h, w, dir = waiting[0]
        waiting = waiting[1:]
        if w < 0 or w >= width or h < 0 or h >= height:
            continue
        if dir in visited[h, w]:
            continue
        waiting += next_steps(h, w, dir, mirrors[h, w])
        visited[h, w] += dir
    
    return (visited != "").sum()

def puzzle2(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    mirrors = np.array([[a for a in line] for line in lines])
    height, width = mirrors.shape
    starts = []
    for i in range(height):
        starts.append((i, 0, "r"))
        starts.append((i, width - 1, "l"))
    for i in range(width):
        starts.append((0, i, "d"))
        starts.append((height - 1, 0, "u"))
    
    result = 0
    for start in starts:
        waiting = [start]
        visited = np.zeros_like(mirrors)
        while len(waiting) > 0:
            h, w, dir = waiting[0]
            waiting = waiting[1:]
            if w < 0 or w >= width or h < 0 or h >= height:
                continue
            if dir in visited[h, w]:
                continue
            waiting += next_steps(h, w, dir, mirrors[h, w])
            visited[h, w] += dir
        
        result = max(result, (visited != "").sum())
    return result

def next_steps(h, w, dir, mirror):
    if dir == "r":
        if mirror in ".-":
            return [(h, w + 1, "r")]
        if mirror == "\\":
            return [(h + 1, w, "d")]
        if mirror == "/":
            return [(h - 1, w, "u")]
        if mirror == "|":
            return [(h, w, "d"), (h, w, "u")]
    
    if dir == "l":
        if mirror in ".-":
            return [(h, w - 1, "l")]
        if mirror == "\\":
            return [(h - 1, w, "u")]
        if mirror == "/":
            return [(h + 1, w, "d")]
        if mirror == "|":
            return [(h, w, "d"), (h, w, "u")]
    
    if dir == "d":
        if mirror in ".|":
            return [(h + 1, w, "d")]
        if mirror == "\\":
            return [(h, w + 1, "r")]
        if mirror == "/":
            return [(h, w - 1, "l")]
        if mirror == "-":
            return [(h, w, "l"), (h, w, "r")]

    if dir == "u":
        if mirror in ".|":
            return [(h - 1, w, "u")]
        if mirror == "\\":
            return [(h, w - 1, "l")]
        if mirror == "/":
            return [(h, w + 1, "r")]
        if mirror == "-":
            return [(h, w, "l"), (h, w, "r")]

def main():

    input_file = open("input16.txt")
    input = input_file.read()

    test_input_1 = """.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = 46
    test_result_2 = 51

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
