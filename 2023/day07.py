import numpy as np

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    pairs = []
    order = "AKQJT98765432"
    for line in lines:
        hand, bid = line.split(" ")
        int_hand = np.array([order.index(a) for a in hand])
        pairs.append([int_hand, int(bid)])

    s = bub_sort(pairs, compare_hands)
    result = 0
    for i in range(len(s)):
        result += s[i][1] * (i+1)
    return result

def puzzle2(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    pairs = []
    order = "AKQT98765432J"
    for line in lines:
        hand, bid = line.split(" ")
        int_hand = np.array([order.index(a) for a in hand])
        pairs.append([int_hand, int(bid)])

    s = bub_sort(pairs, compare_hands_II)
    result = 0
    for i in range(len(s)):
        result += s[i][1] * (i+1)
    return result

def bub_sort(l, c):
    if len(l) <= 1:
        return l
    p = l[0]
    smaller = list(filter(lambda x: c(x, p), l))
    equal = list(filter(lambda x: not c(p, x) and not c(x, p), l))
    bigger = list(filter(lambda x: c(p, x), l))
    return bub_sort(smaller, c) + equal + bub_sort(bigger, c)

def compare_hands(pair1, pair2):
    occurrences1 = np.bincount(pair1[0])
    occurrences2 = np.bincount(pair2[0])
    for i in range(5, 1, -1):
        a1 = np.sum(occurrences1 == i)
        a2 = np.sum(occurrences2 == i)
        if a1 == a2:
            continue
        else:
            return a1 < a2
    return pair1[0].tolist() > pair2[0].tolist()

def compare_hands_II(pair1, pair2):
    occurrences1 = np.bincount(pair1[0], minlength=13)
    occurrences2 = np.bincount(pair2[0], minlength=13)
    js1 = occurrences1[-1]
    js2 = occurrences2[-1]
    occurrences1 = occurrences1[:-1]
    occurrences2 = occurrences2[:-1]
    occurrences1[np.where(occurrences1==occurrences1.max())[0][0]] += js1
    occurrences2[np.where(occurrences2==occurrences2.max())[0][0]] += js2
    for i in range(5, 1, -1):
        a1 = np.sum(occurrences1 == i)
        a2 = np.sum(occurrences2 == i)
        if a1 == a2:
            continue
        else:
            return a1 < a2
    return pair1[0].tolist() > pair2[0].tolist()

def main():

    input_file = open("input07.txt")
    input = input_file.read()

    test_input_1 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = 6440
    test_result_2 = 5905

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()