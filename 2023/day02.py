import numpy as np

def puzzle1(games):
    result = 0
    limit = [12, 13, 14]
    for game in games.keys():
        possible = True
        for set in games[game]:
            for i in range(3):
                if limit[i] < set[i]:
                    possible = False
        if possible:
            result = result + game
    return result

def puzzle2(games):
    result = 0
    for game in games.keys():
        limit = [0, 0, 0]
        possible = True
        for set in games[game]:
            for i in range(3):
                limit[i] = max(set[i], limit[i])
        result = result + limit[0] * limit[1] * limit[2]
    return result

def parse_input(raw_input):
    lines = raw_input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    games = {}
    colors = {"red": 0, "green": 1, "blue": 2}
    for line in lines:
        a = line.find(":")
        game = int (line[5:a])
        sets = line[a+2:].split(";")
        for set in sets:
            cubes = set.split(",")
            games[game] = games.get(game, [])
            games[game].append([0,0,0])
            for cube in cubes:
                pair = cube.strip(" ").split(" ")
                games[game][-1][colors[pair[1]]] = int(pair[0])
    return games

def read_and_parse(filename):
    input_file = open(filename, "r")
    raw_input = input_file.read()
    input = parse_input(raw_input)
    return input

def main():

    input = read_and_parse("input02.txt")

    test_result_1 = 8
    test_input_1 = parse_input("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""")

    test_result_2 = 2286
    test_input_2 = test_input_1

    result_1 = puzzle1(test_input_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()