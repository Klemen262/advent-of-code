import numpy as np
from math import lcm

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    moves = lines[0]
    nettwork = {}
    for line in lines[2:]:
        key, pair = line.split(" = ")
        nettwork[key] = [pair[1:4], pair[6:9]]
    step = 0
    node = "AAA"
    while node != "ZZZ":
        node = nettwork[node][0 if moves[step % len(moves)] == "L" else 1]
        step += 1
    return step

def puzzle2(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    moves = lines[0]
    nettwork = {}
    for line in lines[2:]:
        key, pair = line.split(" = ")
        nettwork[key] = [pair[1:4], pair[6:9]]
    step = 0
    start_nodes = list(filter(lambda x: x[2] == "A", nettwork.keys()))
    steps = []
    for node in start_nodes:
        step = 0
        while node[2] != "Z":
            node = nettwork[node][0 if moves[step % len(moves)] == "L" else 1]
            step += 1
        steps.append(step)
    result = 1
    for s in steps:
        result = lcm(result, s)
    return result


def all_Zs(start_nodes):
    for node in start_nodes:
        if node[2] != "Z":
            return False
    return True

def main():

    input_file = open("input08.txt")
    input = input_file.read()

    test_input_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

    test_input_2 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""
    #test_input_2 = test_input_1

    test_result_1 = 2
    test_result_2 = 6

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
