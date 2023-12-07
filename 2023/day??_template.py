import numpy as np

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    
    return 0

def puzzle2(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    
    return 0

def main():

    input_file = open("input??.txt")
    input = input_file.read()

    test_input_1 = """"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = -1
    test_result_2 = -1

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
