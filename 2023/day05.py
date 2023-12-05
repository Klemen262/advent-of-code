import numpy as np

def puzzle1(input):
    prev_category, convs = input
    new_category = []
    for conv in convs:
        for el in prev_category:
            found = False
            for line in conv:
                if el >= line[1] and el < line[1] + line[2]:
                    new_category.append(el + line[0] - line[1])
                    found = True
                    break
            if not found:
                new_category.append(el)
        prev_category = new_category
        new_category = []
    return min(prev_category)

def puzzle2(input):
    prev_category, convs = input
    old_pairs = []
    for i in range(len(prev_category)//2):
        a, b = prev_category[2*i:2*i+2]
        old_pairs.append([a, a+b])
    old_pairs.sort()
    for conv in convs:
        new_pairs = []
        conv_ranges = []
        for line in conv:
            conv_ranges.append([line[1], line[1] + line[2], line[0] - line[1]])
        conv_ranges.sort()
        conv_range = conv_ranges[0]
        conv_ranges = conv_ranges[1:]
        while len(old_pairs) > 0:
            pair = old_pairs[0]
            old_pairs = old_pairs[1:]
            start = pair[0]
            end = pair[1]
            while conv_range[1] <= start and len(conv_ranges) > 0:
                conv_range = conv_ranges[0]
                conv_ranges = conv_ranges[1:]
            conv_start = conv_range[0]
            conv_end = conv_range[1]
            shift = conv_range[2]
            if start < conv_start:
                if end <= conv_start:
                    new_pairs.append(pair)
                else:
                    new_pairs.append([start, conv_start])
                    old_pairs = [[conv_start, end]] + old_pairs
            elif start >= conv_start and start < conv_end:
                if end <= conv_end:
                    new_pairs.append([start + shift, end + shift])
                else:
                    new_pairs.append([start + shift, conv_end + shift])
                    old_pairs = [[conv_end, end]] + old_pairs
            else:
                new_pairs.append([start, end])
        old_pairs = sorted(new_pairs)
    return min(old_pairs)[0]

def parse_input(raw_input):
    groups = raw_input.split("\n\n")
    seeds = [int(a) for a in groups[0].split(" ")[1:]]
    conversions = []
    for group in groups[1:]:
        lines = group.split("\n")[1:]
        if lines[-1] == "":
            lines = lines[:-1]
        conv = []
        for line in lines:
            numbers = [int(a) for a in line.split(" ")]
            conv.append(numbers)
        conversions.append(conv)
    return seeds, conversions

def read_and_parse(filename):
    input_file = open(filename, "r")
    raw_input = input_file.read()
    input = parse_input(raw_input)
    return input

def main():

    input = read_and_parse("input05.txt")

    test_result_1 = 35
    test_input_1 = parse_input("""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""")

    test_result_2 = 46
    #test_input_2 = parse_input("""""")
    test_input_2 = test_input_1

    result_1 = puzzle1(test_input_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()