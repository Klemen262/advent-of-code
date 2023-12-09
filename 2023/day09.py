import numpy as np

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    result = 0
    for line in lines:
        values = np.array([int(a) for a in line.split(" ")])
        while values[values == 0].size != values.size:
            result += values[-1]
            values = values[1:] - values[:-1]
    return result

def puzzle2(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    result = 0
    for line in lines:
        values = np.array([int(a) for a in line.split(" ")])
        first = []
        while values[values == 0].size != values.size:
            first.append(values[0])
            values = values[1:] - values[:-1]
        result += sum(first[::2])
        result -= sum(first[1::2])
    return result


def main():

    input_file = open("input09.txt")
    input = input_file.read()

    test_input_1 = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = 114
    test_result_2 = 2

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
