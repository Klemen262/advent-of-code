import numpy as np

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
        result = 0
    for line in lines:
        record, groups = line.split(" ")
        sizes = [int(a) for a in groups.split(",")]
        result +=arangements(record, np.array(sizes))
    return result

def arangements(record: np.ndarray, sizes: np.ndarray):
    if len(record) < sizes.sum():
        return 0
    if sizes.size == 0:
        if len(record) == 0:
            return 1
        elif record.find("#") == -1:
            return 1
        else:
            return 0
    elif len(record) == 0:
        return 0
    result = 0
    i = 0
    size = sizes[0]
    for i in range(len(record) - size + 1):
        r = record[i]
        if r == "#":
            ok = True
            for a in range(1, size):
                if record[i + a] == ".":
                    ok = False
                    break
            if ok and (i + size == len(record) or record[i + size] != "#"):
                result += arangements(record[i + size + 1:], sizes[1:])
            return result
        elif r == "?":
            ok = True
            for a in range(1, size):
                if record[i + a] == ".":
                    ok = False
                    break
            if ok and i + size == len(record):
                result += arangements(record[i + size + 1:], sizes[1:])
            elif ok and record[i + size] != "#":
                result += arangements(record[i + size + 1:], sizes[1:])
    return result

def puzzle2(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
        result = 0
    for line in lines:
        record, groups = line.split(" ")
        sizes = [int(a) for a in groups.split(",")]
        record = "?".join([record] * 5)
        sizes = np.tile(sizes, 5)
        r = arangements(record, np.array(sizes))
        result += r
    return result

def main():

    input_file = open("input12.txt")
    input = input_file.read()

    test_input_1 = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = 21
    test_result_2 = 525152

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
