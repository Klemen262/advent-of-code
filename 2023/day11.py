import numpy as np

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    sky = []
    for line in lines:
        skyline = []
        for a in line:
            skyline.append(0 if a == "." else 1)
        sky.append(skyline)
    sky = np.array(sky)
    column_galaxies = sky.sum(axis=0)
    row_galaxies = sky.sum(axis=1)
    gal_h, gal_w = np.where(sky == 1)
    result = 0
    for i in range(len(gal_h)):
        for j in range(i+1, len(gal_h)):
            h1 = gal_h[i]
            w1 = gal_w[i]
            h2 = gal_h[j]
            w2 = gal_w[j]
            dist = abs(h1-h2) + (row_galaxies[min(h1, h2) : max(h1, h2)] == 0).sum()
            dist += abs(w1-w2) + (column_galaxies[min(w1, w2) : max(w1, w2)] == 0).sum()
            result += dist
    return result

def puzzle2(input, expansion):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    sky = []
    for line in lines:
        skyline = []
        for a in line:
            skyline.append(0 if a == "." else 1)
        sky.append(skyline)
    sky = np.array(sky)
    column_galaxies = sky.sum(axis=0)
    row_galaxies = sky.sum(axis=1)
    gal_h, gal_w = np.where(sky == 1)
    result = 0
    for i in range(len(gal_h)):
        for j in range(i+1, len(gal_h)):
            h1 = gal_h[i]
            w1 = gal_w[i]
            h2 = gal_h[j]
            w2 = gal_w[j]
            dist = abs(h1-h2) + (row_galaxies[min(h1, h2) : max(h1, h2)] == 0).sum() * (expansion - 1)
            dist += abs(w1-w2) + (column_galaxies[min(w1, w2) : max(w1, w2)] == 0).sum() * (expansion - 1)
            result += dist
    return result

def main():

    input_file = open("input11.txt")
    input = input_file.read()

    test_input_1 = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = 374
    test_result_2 = 8410

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2, 100)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input, 1000000)) + '\033[0m')

if __name__ == "__main__":
    main()
