import numpy as np

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    dirs = np.array([line[0] for line in lines])
    steps = np.array([int(line.split(" ")[1]) for line in lines])
    lr = (steps * (dirs == "R") - steps * (dirs == "L")).cumsum()
    left = lr.min()
    right = lr.max()
    ud = (steps * (dirs == "D") - steps * (dirs == "U")).cumsum()
    up = ud.min()
    down = ud.max()
    ground = np.zeros((down - up + 1, right - left + 1), dtype=int)
    h = -up
    w = -left
    for nh, nw in zip(ud + h, lr + w):
        hm = min(h, nh)
        hM = max(h, nh)
        wm = min(w, nw)
        wM = max(w, nw)
        ground[hm:hM+1,wm:wM+1] = 1
        h, w = nh, nw
    ground[0, ground[0,:] == 0] = 2
    ground[-1, ground[-1,:] == 0] = 2
    ground[ground[:,0] == 0, 0] = 2
    ground[ground[:,-1] == 0, -1] = 2
    pout = 0
    out = (ground == 2).sum()
    while out > pout:
        ground[:-1,:][(ground[:-1,:] == 0) * (ground[1:,:] == 2)] = 2
        ground[1:,:][(ground[1:,:] == 0) * (ground[:-1,:] == 2)] = 2
        ground[:,:-1][(ground[:,:-1] == 0) * (ground[:,1:] == 2)] = 2
        ground[:,1:][(ground[:,1:] == 0) * (ground[:,:-1] == 2)] = 2
        pout = out
        out = (ground == 2).sum()
    return (ground != 2).sum()

def hex_to_dec(h):
    result = 0
    values = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, 
              "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, 
              "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    for a in h:
        result *= 16
        result += values[a]
    return result

def puzzle2(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    hexs = [line.split(" ")[2] for line in lines]
    steps = np.array([hex_to_dec(h[2:-2]) for h in hexs])
    dirs = np.array([h[-2] for h in hexs])
    w = 0
    surface = 1
    for i in range(len(steps)):
        if dirs[i] == "1":
            surface += steps[i] * (w + 1)
        elif dirs[i] == "3":
            surface -= steps[i] * w
        elif dirs[i] == "2":
            w -= steps[i]
        elif dirs[i] == "0":
            surface += steps[i]
            w += steps[i]
    return surface

def main():

    input_file = open("input18.txt")
    input = input_file.read()

    test_input_1 = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = 62
    test_result_2 = 952408144115

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
