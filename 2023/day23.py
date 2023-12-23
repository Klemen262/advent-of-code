import numpy as np
import sys

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    maze = np.array([[a for a in line] for line in lines])
    sys.setrecursionlimit(maze.size)
    best = [0]
    max_hike(0, 1, maze, True, best)
    return best[0]

def puzzle2(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    maze = np.array([[a for a in line] for line in lines])
    sys.setrecursionlimit(maze.size)
    best = [0]
    max_hike(0, 1, maze, False, best)
    return best[0]

def max_hike(h, w, maze, part_one, best):
    height, width = maze.shape
    previous_tile = maze[h, w]
    nbhs = find_neighbours(h, w, maze, part_one)
    maze[h, w] = "o"
    if len(nbhs) == 0 and h == height - 1 and w == width - 2:
        path_len = (maze=="o").sum() - 1
        if path_len > best[0]:
            best[0] = path_len
    for nh, nw in nbhs:
        max_hike(nh, nw, maze, part_one, best)
    maze[h, w] = previous_tile

def find_neighbours(h, w, maze, part_one):
    nbh = []
    if part_one:
        if maze[h, w] == "<":
            nbh = [(h, w - 1)]
        elif maze[h, w] == ">":
            nbh = [(h, w + 1)]
        elif maze[h, w] == "v":
            nbh = [(h + 1, w)]
        elif maze[h, w] == "^":
            nbh = [(h - 1, w)]
        if len(nbh) == 1:
            if maze[nbh[0]] in "#o":
                return []
            else:
                return nbh
    height, width = maze.shape
    for a, b in [(h - 1, w), (h + 1, w), (h, w - 1), (h, w + 1)]:
        if a >= 0 and a < height and b >= 0 and b < width:
            if maze[a, b] not in "#o":
                nbh.append((a, b))
    return nbh

# In the morning, I didn't have time to finish optimizations for second part.
# Before I came back to programming, my laptop finished caluculating the answer with original function :)
# It took 596 minutes.

#def puzzle2_2(input):
#    lines = input.split("\n")
#    if lines[-1] == "":
#        lines = lines[:-1]
#    maze = np.array([[a for a in line] for line in lines])
#    sys.setrecursionlimit(maze.size)
#
#    choices = {}
#    calculated = set()
#    intersections = [((0, 1), [(1, 1)])]
#    while len(intersections) > 0:
#        start, nbhs = intersections[0]
#        sh, sw = start
#        intersections = intersections[1:]
#        if start in calculated:
#            continue
#        calculated.add(start)
#        previous_tile = maze[sh, sw]
#        maze[sh, sw] = "o"
#        for nbh in nbhs:
#            res = find_path_to_first_intersection(nbh, maze, False)
#            if res != None:
#                l, next_node, nbhs = res
#                intersections.append((next_node, nbhs))
#                choices_here = choices.get(start, [])
#                choices_here.append((l, next_node))
#                choices[start] = choices_here
#        maze[sh, sw] = previous_tile
#    
#    print(choices)
#
#    return 0
#
#def find_path_to_first_intersection(start, maze, part_one):
#    h, w = start
#    height, width = maze.shape
#    previous_tile = maze[h, w]
#    nbhs = find_neighbours(h, w, maze, part_one)
#    maze[h, w] = "o"
#    if len(nbhs) == 1:
#        nh, nw = nbhs[0]
#        result = find_path_to_first_intersection((nh, nw), maze, part_one)
#    elif len(nbhs) > 1:
#        path_len = (maze=="o").sum() - 1
#        result = (path_len, (h, w), nbhs)
#    elif h == height - 1 and w == width - 2:
#        path_len = (maze=="o").sum() - 1
#        result = (path_len, (h, w), [])
#    else:
#        result = None
#    maze[h, w] = previous_tile
#    return result

def main():

    input_file = open("input23.txt")
    input = input_file.read()

    test_input_1 = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = 94
    test_result_2 = 154

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
