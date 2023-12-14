import numpy as np

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    platform = np.array([[0 if a == "." else (1 if a == "#" else 2) for a in line] for line in lines])
    hs, ws = np.where(platform == 2)
    height = platform.shape[0]
    load = 0
    for i in range(hs.size):
        h = hs[i]
        w = ws[i]
        above = platform[:h, w][::-1]
        cubes = np.where(above == 1)[0]
        top = above.size
        if cubes.size > 0:
            top = cubes[0]
        rounds = (above[: top] == 2).sum()
        load_here = (top - rounds) + (height - h)
        load += load_here
    return load

def north_load(platform):
    hs, ws = np.where(platform == 2)
    height = platform.shape[0]
    load = 0
    for i in range(hs.size):
        h = hs[i]
        w = ws[i]
        load_here = (height - h)
        load += load_here
    return load

def puzzle2(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    platform = np.array([[0 if a == "." else (1 if a == "#" else 2) for a in line] for line in lines])

    previous_platforms = []
    previous_loads = []
    cycles = 1000000000
    for round in range(cycles):
        for direction in range(4):
            next = np.zeros_like(platform)
            next[platform == 1] = 1
            hs, ws = np.where(platform == 2)
            height = platform.shape[0]
            for i in range(hs.size):
                h = hs[i]
                w = ws[i]
                above = platform[:h, w][::-1]
                cubes = np.where(above == 1)[0]
                top = above.size
                if cubes.size > 0:
                    top = cubes[0]
                rounds = (above[: top] == 2).sum()
                load_here = (top - rounds) + (height - h)
                next[height - load_here, w] = 2
            platform = next.T[:, ::-1]
        
        load = north_load(platform)

        for idx in np.where(np.array(previous_loads) == load)[0]:
            if ((previous_platforms[idx] - platform) != 0).sum() == 0:
                to_go = cycles - round
                to_go_from_now = to_go % (round - idx)
                if to_go_from_now == 0:
                    index_of_last = idx
                else:
                    index_of_last = to_go_from_now + idx - 1
                result = previous_loads[index_of_last]
                return result
        
        previous_platforms.append(platform)
        previous_loads.append(load)

    return load

def main():

    input_file = open("input14.txt")
    input = input_file.read()

    test_input_1 = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = 136
    test_result_2 = 64

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
