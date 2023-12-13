import numpy as np

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    mirrors = "\n".join(lines).split("\n\n")
    result = 0
    for mirror in mirrors:
        reflection = np.array([[0 if a == "." else 1 for a in line] for line in mirror.split("\n")])
        solved = False
        cols = reflection.sum(axis=0)
        diff = cols[1:] - cols[:-1]
        candidates = np.where(diff == 0)[0]
        n = diff.size
        for c in candidates + 1:
            l = min(c, n - c + 1)
            if (reflection[:,c-l:c] - reflection[:,c:c+l:][:,::-1] != 0).sum() == 0:
                result += c
                solved = True
                break
        
        if not solved:
            rows = reflection.sum(axis=1)
            diff = rows[1:] - rows[:-1]
            candidates = np.where(diff == 0)[0]
            n = diff.size
            for c in candidates + 1:
                l = min(c, n - c + 1)
                if (reflection[c-l:c, :] - reflection[c:c+l, :][::-1,:] != 0).sum() == 0:
                    result += c * 100
                    solved = True
                    break
    return result

def puzzle2(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    mirrors = "\n".join(lines).split("\n\n")
    result = 0
    for mirror in mirrors:
        reflection = np.array([[0 if a == "." else 1 for a in line] for line in mirror.split("\n")])
        solved = False
        cols = reflection.sum(axis=0)
        diff = cols[1:] - cols[:-1]
        candidates = np.where(abs(diff) <= 1)[0]
        n = diff.size
        for c in candidates + 1:
            l = min(c, n - c + 1)
            if (reflection[:,c-l:c] - reflection[:,c:c+l:][:,::-1] != 0).sum() == 1:
                result += c
                solved = True
                break
        
        if not solved:
            rows = reflection.sum(axis=1)
            diff = rows[1:] - rows[:-1]
            candidates = np.where(abs(diff) <= 1)[0]
            n = diff.size
            for c in candidates + 1:
                l = min(c, n - c + 1)
                if (reflection[c-l:c, :] - reflection[c:c+l, :][::-1,:] != 0).sum() == 1:
                    result += c * 100
                    solved = True
                    break
    return result

def main():

    input_file = open("input13.txt")
    input = input_file.read()

    test_input_1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = 405
    test_result_2 = 400

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
