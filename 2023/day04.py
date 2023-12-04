import numpy as np

def puzzle1(input):
    winning, i_have = input
    result = 0
    for i in range(len(winning)):
        match = winning[i].intersection(i_have[i])
        n = len(match)
        result += 2 ** n // 2
    return result

def puzzle2(input):
    winning, i_have = input
    copies = np.ones((len(winning)), dtype=int)
    for i in range(len(winning)):
        match = winning[i].intersection(i_have[i])
        n = len(match)
        copies[i+1:i+1+n] += copies[i]
    return sum(copies)


def parse_input(raw_input):
    lines = raw_input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    both = [line.split(": ")[1].split(" | ") for line in lines]
    winning = [set(a[0].split(" ")) for a in both]
    i_have = [set(a[1].split(" ")) for a in both]
    for i in range(len(winning)):
        if "" in winning[i]:
            winning[i].remove("")
        if "" in i_have[i]:
            i_have[i].remove("")
    return winning, i_have

def read_and_parse(filename):
    input_file = open(filename, "r")
    raw_input = input_file.read()
    input = parse_input(raw_input)
    return input

def main():

    input = read_and_parse("input04.txt")

    test_result_1 = 13
    test_input_1 = parse_input("""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""")

    test_result_2 = 30
    test_input_2 = test_input_1

    result_1 = puzzle1(test_input_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()