import numpy as np

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    result = 0
    for line in lines[0].split(","):
        my_hash = 0
        for char in line:
            my_hash = (my_hash + ord(char)) * 17 % 256
        result += my_hash
    return result

def puzzle2(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    boxes = []
    for _ in range(256):
        boxes.append([[],[]])
    for line in lines[0].split(","):
        remove = False
        if line[-1] == "-":
            label = line[:-1]
            remove = True
        else:
            label, focal_lenght = line.split("=")
            focal_lenght = int(focal_lenght)
        my_hash = 0
        for char in label:
            my_hash = (my_hash + ord(char)) * 17 % 256
        labels, focals = boxes[my_hash]
        if remove:
            if label in labels:
                idx = labels.index(label)
                del labels[idx]
                del focals[idx]
        else:
            if label in labels:
                idx = labels.index(label)
                labels[idx] = label
                focals[idx] = focal_lenght
            else:
                labels.append(label)
                focals.append(focal_lenght)
    
    result = 0
    for box in range(256):
        for slot in range(len(boxes[box][0])):
            focal_power = (box + 1) * (slot + 1) * boxes[box][1][slot]
            result += focal_power
    return result

def main():

    input_file = open("input15.txt")
    input = input_file.read()

    test_input_1 = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = 1320
    test_result_2 = 145

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
