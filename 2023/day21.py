import numpy as np

def puzzle1(input, steps):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    garden = np.array([[a for a in line] for line in lines])
    neighbours = {}
    hs, ws = np.where(garden != "#")
    for h, w, in zip(hs, ws):
        neighbours[(h, w)] = find_neighbours(h, w, garden)
    start = np.where(garden == "S")
    queue = set()
    queue.add((start[0][0], start[1][0]))
    for i in range((steps)):
        new_queue = set()
        for h, w in queue:
            for nbh in neighbours[(h, w)]:
                new_queue.add(nbh)
        queue = new_queue
    return len(queue)

def puzzle2(input):
    steps = 26501365

    repeats = steps // 131

    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    garden = np.array([[a for a in line] for line in lines])
    
    start = np.where(garden == "S")
    start = (start[0][0], start[1][0])
    new_garden = garden.copy()
    new_garden[start] = "."
    mins = minimum_steps(garden)

    odd_even = 0 if steps % 2 == 1 else 1

    inner_even = ((mins != -1) * (mins % 2 == odd_even) * (garden != "#") * (mins <= 65)).sum()
    inner_odd = ((mins != -1) * (mins % 2 == (1 - odd_even)) * (garden != "#") * (mins <= 65)).sum()
    outer_even = ((mins != -1) * (mins % 2 == (1 - odd_even)) * (garden != "#") * (mins > 65)).sum()
    outer_odd = ((mins != -1) * (mins % 2 == odd_even) * (garden != "#") * (mins > 65)).sum()

    odd_even = 1 if repeats % 2 == 0 else 0

    result = 0
    result += (repeats + odd_even) ** 2 * inner_odd
    result += (repeats + (1 - odd_even)) ** 2 * inner_even
    result += repeats * (repeats + 1) * (outer_even + outer_odd)
    return result

def find_neighbours(h, w, garden):
    height, width = garden.shape
    nbh = []
    for a, b in [(h - 1, w), (h + 1, w), (h, w - 1), (h, w + 1)]:
        if a >= 0 and a < height and b >= 0 and b < width:
            if garden[a, b] != "#":
                nbh.append((a, b))
    return nbh

def minimum_steps(garden):
    neighbours = {}
    hs, ws = np.where(garden != "#")
    for h, w, in zip(hs, ws):
        neighbours[(h, w)] = find_neighbours(h, w, garden)
    min_steps = np.zeros(garden.shape, dtype=int) - 1

    start = np.where(garden == "S")
    start = (start[0][0], start[1][0])
    queue = set()
    queue.add(start)
    min_steps[start] = 0
    i = 1
    while len(queue) > 0:
        new_queue = set()
        for h, w in queue:
            for nbh in neighbours[(h, w)]:
                if min_steps[nbh] == -1:
                    min_steps[nbh] = i
                    new_queue.add(nbh)
        queue = new_queue
        i += 1
    return min_steps

def main():

    input_file = open("input21.txt")
    input = input_file.read()

    test_input_1 = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""

    test_result_1 = 16
    test_steps = 6
    steps = 64

    result_1 = puzzle1(test_input_1, test_steps)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input, steps)) + '\033[0m')

    print('\033[92m' + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
