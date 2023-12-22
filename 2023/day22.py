import numpy as np

def puzzle1(input):
    n, supported_by = parse(input)

    unsafe = set()
    for brick in supported_by.keys():
        sup = supported_by[brick]
        sup = sup[sup != 0]
        if sup.size == 1:
            unsafe.add(sup[0])
    return n - len(unsafe)

def puzzle2(input):
    n, supported_by = parse(input)

    is_supporting = {}

    for brick_number in range(1, n + 1):
        for upper in supported_by[brick_number]:
            is_supporting[upper] = is_supporting.get(upper, set())
            is_supporting[upper].add(brick_number)

    result = 0
    for brick_number in range(1, n + 1):
        falling = set()
        new_falling = set()
        new_falling.add(brick_number)
        while len(new_falling) > 0:
            falling = falling.union(new_falling)
            new_falling = set()
            for fall in falling:
                for b in is_supporting.get(fall, []):
                    if len(set(supported_by[b]).difference(falling)) == 0 and b not in falling:
                        new_falling.add(b)
        result += len(falling) - 1
    return result

def parse(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    brick_number = 1
    n = len(lines)
    bricks = np.zeros((n, 2, 3), dtype=int)
    for line in lines: 
        start, end = line.split("~")
        sx, sy, sz = [int(a) for a in start.split(",")]
        ex, ey, ez = [int(a) for a in end.split(",")]
        bricks[brick_number - 1, :, :] = [[sx, sy, sz], [ex, ey, ez]]
        brick_number += 1
    dimensions = bricks.max(axis=(0, 1)) + (1, 1, 2)
    container = np.zeros(dimensions, dtype=int) - 1
    container[:, :, 0] = 0
    brick_indices = []

    for brick_number in range(1, n + 1):
        sx, sy, sz = bricks[brick_number - 1, 0, :]
        ex, ey, ez = bricks[brick_number - 1, 1, :]
        mx = min(sx, ex)
        my = min(sy, ey)
        mz = min(sz, ez)
        Mx = max(sx, ex) + 1
        My = max(sy, ey) + 1
        Mz = max(sz, ez) + 1
        brick_indices.append((np.arange(mx, Mx), np.arange(my, My), np.arange(mz, Mz)))
        container[mx:Mx, my:My, mz:Mz] = brick_number

    supported_by = {}
    z = 1
    while z < dimensions[2]:
        bricks_in_this_layer = np.unique(container[:, :, z])
        for brick in bricks_in_this_layer:
            if brick == -1:
                continue
            if supported_by.get(brick, None) == None:
                descent = 0
                # finds, how deep it can fall before hitting another block
                below_block = container[:, :, z - descent - 1][container[:, :, z] == brick]
                while (below_block != -1).sum() == 0:
                    descent += 1
                    below_block = container[:, :, z - descent - 1][container[:, :, z] == brick]
                supported_by[brick] = np.unique(below_block[below_block != -1])
                indices = brick_indices[brick - 1]
                container[indices] = -1
                container[indices[0], indices[1], indices[2] - descent] = brick
        z += 1
    return n, supported_by

def main():

    input_file = open("input22.txt")
    input = input_file.read()

    test_input_1 = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = 5
    test_result_2 = 7

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
