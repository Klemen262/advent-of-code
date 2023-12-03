import numpy as np

def puzzle1(schema):
    h, w = schema.shape
    result = 0
    for i in range(h):
        number = 0
        is_part_number = False
        for j in range(w):
            a = schema[i, j]
            if a in "0123456789":
                number *= 10
                number += int(a)
                is_part_number = is_part_number or is_part(schema, i, j)
            else:
                if is_part_number:
                    result += number
                number = 0
                is_part_number = False
        if is_part_number:
            result += number
        number = 0
        is_part_number = False
    return result

def is_part(schema, i, j):
    a = "".join(neighbours(schema, i, j))
    a = a.replace(".", "")
    for i in range(10):
        a = a.replace(str(i), "")
    return len(a) > 0

def neighbours(schema, i, j):
    h, w = schema.shape
    neighbours = []
    if i > 0:
        neighbours.append(schema[i-1, j])
        if j > 0:
            neighbours.append(schema[i-1, j-1])
        if j < w-1:
            neighbours.append(schema[i-1, j+1])
    if i < h-1:
        neighbours.append(schema[i+1, j])
        if j > 0:
            neighbours.append(schema[i+1, j-1])
        if j < w-1:
            neighbours.append(schema[i+1, j+1])
    if j > 0:
        neighbours.append(schema[i, j-1])
    if j < w-1:
        neighbours.append(schema[i, j+1])
    return neighbours


def parse(schema, i, j):
    h, w = schema.shape
    numbers = "0123456789"
    number = 0
    while j >= 0 and schema[i, j] in numbers:
        j -= 1
    j += 1
    while j < w and schema[i, j] in numbers:
        number *= 10
        number += int(schema[i, j])
        j += 1
    return number


def gear_ratio(schema, i, j):
    h, w = schema.shape
    if schema[i, j] != "*":
        return 0
    adjecent_part_numbers = 0
    numbers = "0123456789"
    product = 1
    if i > 0:
        if schema[i-1, j] in numbers:
            adjecent_part_numbers += 1
            product *= parse(schema, i-1, j)
        else:
            if j > 0:
                if schema[i-1, j-1] in numbers:
                    adjecent_part_numbers += 1
                    product *= parse(schema, i-1, j-1)
            if j < w-1:
                if schema[i-1, j+1] in numbers:
                    adjecent_part_numbers += 1
                    product *= parse(schema, i-1, j+1)
    if i < h-1:
        if schema[i+1, j] in numbers:
            adjecent_part_numbers += 1
            product *= parse(schema, i+1, j)
        else:
            if j > 0:
                if schema[i+1, j-1] in numbers:
                    adjecent_part_numbers += 1
                    product *= parse(schema, i+1, j-1)
            if j < w-1:
                if schema[i+1, j+1] in numbers:
                    adjecent_part_numbers += 1
                    product *= parse(schema, i+1, j+1)
    if j > 0:
        if schema[i, j-1] in numbers:
            adjecent_part_numbers += 1
            product *= parse(schema, i, j-1)
    if j < w-1:
        if schema[i, j+1] in numbers:
            adjecent_part_numbers += 1
            product *= parse(schema, i, j+1)
    if adjecent_part_numbers == 2:
        return product
    else:
        return 0


def puzzle2(schema):
    h, w = schema.shape
    result = 0
    gears = np.zeros_like(schema)
    for i in range(h):
        for j in range(w):
            result += gear_ratio(schema, i, j)
    return result

def parse_input(raw_input):
    lines = raw_input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    schema = np.array([[znak for znak in line] for line in lines])
    return schema

def read_and_parse(filename):
    input_file = open(filename, "r")
    raw_input = input_file.read()
    input = parse_input(raw_input)
    return input

def main():

    input = read_and_parse("input03.txt")

    test_result_1 = 4361
    test_input_1 = parse_input("""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""")

    test_result_2 = 467835
    test_input_2 = test_input_1

    result_1 = puzzle1(test_input_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()