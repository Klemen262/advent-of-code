import numpy as np

def puzzle1(input):
    times, distances = input
    result = 1
    for i in range(len(times)):
        distance = distances[i]
        time = times[i]
        speed = np.arange(time)
        traveled = speed * (time - speed)
        ways = np.sum(traveled > distance)
        result *= ways
    return result

def puzzle2(input):
    times, distances = input
    time = int("".join([str(a) for a in (times)]))
    distance = int("".join([str(a) for a in (distances)]))
    return puzzle1(([time], [distance]))

def parse_input(raw_input):
    lines = raw_input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    times = np.array([int(a) for a in filter(lambda x: x >= x != "", lines[0].split(":")[1].split(" "))])
    distances = np.array([int(a) for a in filter(lambda x: x >= x != "", lines[1].split(":")[1].split(" "))])
    return times, distances

def read_and_parse(filename):
    input_file = open(filename, "r")
    raw_input = input_file.read()
    input = parse_input(raw_input)
    return input

def main():

    input = read_and_parse("input06.txt")

    test_result_1 = 288
    test_input_1 = parse_input("""Time:      7  15   30
Distance:  9  40  200""")

    test_result_2 = 71503
    #test_input_2 = parse_input("""""")
    test_input_2 = test_input_1

    result_1 = puzzle1(test_input_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()