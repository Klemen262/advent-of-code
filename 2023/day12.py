import numpy as np
from math import comb

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
        result = 0
    for line in lines:
        record, groups = line.split(" ")
        sizes = [int(a) for a in groups.split(",")]
        r = arangements(record, np.array(sizes))
        result += r
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
        results = np.zeros((len(record), len(sizes)), dtype=int) - 1
        r4 = arangements4(record, np.array(sizes), 0, 0, results)
        result += r4
    return result

def fac(n):
    if n <= 1:
        return 1
    else:
        return n * fac(n - 1)

def my_comb(places, sizes):
    damaged = sizes.sum()
    operational = places - damaged
    free = operational - (sizes.size - 1)
    borders = sizes.size
    if free < 0:
        return 0
    result = comb(free + borders, borders)
    return result

# still too slow
def arangements3(record: np.ndarray, sizes: np.ndarray):
    if sizes.size == 0:
        if "#" in record:
            return 0
        else:
            return 1
    elif len(record) == 0:
        return 0
    
    i = 0
    r = record[i]
    i += 1

    while r == "." and i < len(record):
        r = record[i]
        i += 1
    i -= 1

    if r == ".":
        return 0
    
    record = record[i:]
    i = 0
    r = record[i]

    if r == "#":
        first_size = sizes[0]
        if "." in record[:first_size]:
            return 0
        elif len(record) < first_size or (len(record) > first_size and record[first_size] == "#"):
            return 0
        else:
            return arangements3(record[first_size + 1:], sizes[1:])
    
    while r == "?" and i < len(record):
        r = record[i]
        i += 1
    
    if r == "?":
        return my_comb(i, sizes)
    i -= 1
    if r == ".":
        result = 0
        n = 1
        s = sizes[:n]
        damaged = s.sum()
        while n <= sizes.size and damaged + n - 1 <= i:
            result += my_comb(i, s) * arangements3(record[i:], sizes[n:])
            n += 1
            s = sizes[:n]
            damaged = s.sum()
        result += arangements3(record[i + 1:], sizes)
        return result
    
    else: # r == "#"
        result = 0
        n = 0
        while True:
            s = sizes[:n]
            last = sizes[n]
            damaged = s.sum()
            new_sizes = sizes[n:].copy()
            for start_at in range(max(0, i - last + 1),  min(i, len(record) - last) + 1):
                new_sizes[0] = last + start_at - i
                after = arangements3(record[i:], new_sizes)
                if n == 0:
                    result += after
                elif start_at - 1  >= 0:
                    result += my_comb(start_at - 1, s) * after
            n += 1
            if n >= sizes.size or damaged + s.size > i:
                break
        return result

def arangements4(record: np.ndarray, sizes: np.ndarray, record_index, sizes_index, results):
    if record_index >= len(record):
        if sizes_index >= sizes.size:
            return 1
        else:
            return 0
    else:
        if sizes_index >= sizes.size:
            if record[record_index:].find("#") != -1:
                return 0
            else:
                return 1

    a = results[record_index, sizes_index] 
    if a != -1:
        return a
    
    record_here = record[record_index:]
    sizes_here = sizes[sizes_index:]
    
    if len(record_here) < sizes_here.sum():
        results[record_index, sizes_index] = 0
        return 0
    if sizes_here.size == 0:
        if len(record_here) == 0:
            results[record_index, sizes_index] = 1
            return 1
        elif record_here.find("#") == -1:
            results[record_index, sizes_index] = 1
            return 1
        else:
            results[record_index, sizes_index] = 0
            return 0
    elif len(record_here) == 0:
        results[record_index, sizes_index] = 0
        return 0
    result = 0
    i = 0
    size = sizes_here[0]
    for i in range(len(record_here) - size + 1):
        r = record_here[i]
        if r == "#":
            ok = True
            for a in range(1, size):
                if record_here[i + a] == ".":
                    ok = False
                    break
            if ok and (i + size == len(record_here) or record_here[i + size] != "#"):
                result += arangements4(record, sizes, record_index + i + size + 1, sizes_index + 1, results)
            results[record_index, sizes_index] = result
            return result
        elif r == "?":
            ok = True
            for a in range(1, size):
                if record_here[i + a] == ".":
                    ok = False
                    break
            if ok and i + size == len(record_here):
                result += arangements4(record, sizes, record_index + i + size + 1, sizes_index + 1, results)
            elif ok and record_here[i + size] != "#":
                result += arangements4(record, sizes, record_index + i + size + 1, sizes_index + 1, results)
    results[record_index, sizes_index] = result
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
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
