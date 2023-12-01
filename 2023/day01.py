import numpy as np

def puzzle1(lines):
    sum = 0
    first = False
    for line in lines:
        for znak in line:
            if znak in "123456789":
                if not first:
                    sum += int(znak) * 10
                    first = True
                num = int(znak)
        first = False
        sum += num
    return sum

def puzzle2(lines):
    sum = 0
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in lines:
        indexes_w = [line.find(a) for a in words]
        indexes_w = [10000000000 if a == -1 else a for a in indexes_w]
        indexes_n = [line.find(a) for a in "123456789"]
        indexes_n = [10000000000 if a == -1 else a for a in indexes_n]
        min_i_w = min(indexes_w)
        min_i_n = min(indexes_n)
        number_w = indexes_w.index(min_i_w)
        number_n = indexes_n.index(min_i_n)
        previous_sum = sum
        if min_i_n < min_i_w:
            sum += (number_n + 1) * 10
        else:
            sum += (number_w + 1) * 10
        
        indexes_w = [line[::-1].find(a[::-1]) for a in words]
        indexes_w = [10000000000 if a == -1 else a for a in indexes_w]
        indexes_n = [line[::-1].find(a) for a in "123456789"]
        indexes_n = [10000000000 if a == -1 else a for a in indexes_n]
        min_i_w = min(indexes_w)
        min_i_n = min(indexes_n)
        number_w = indexes_w.index(min_i_w)
        number_n = indexes_n.index(min_i_n)
        if min_i_n < min_i_w:
            sum += (number_n + 1)
        else:
            sum += (number_w + 1)

        #print(sum - previous_sum)
    return sum

def parse_input(raw_input):
    lines = raw_input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    return lines

def read_and_parse(filename):
    input_file = open(filename, "r")
    raw_input = input_file.read()
    input = parse_input(raw_input)
    return input

def main():

    input = read_and_parse("input01.txt")

    test_result_1 = 142
    test_input_1 = parse_input("""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""")

    test_result_2 = 281
    test_input_2 = parse_input("""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""")

    result_1 = puzzle1(test_input_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()