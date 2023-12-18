import numpy as np

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    loss = np.array([[int(a) for a in l] for l in lines])
    height, width = loss.shape
    # h, w, dir (0 r, 1 u, 2 l, 3 d), move
    prices = np.zeros((height, width, 4, 3), dtype=int)
    i = 1
    prices[:, :-i, 0, 0] = loss[:,i:]
    prices[i:, :, 1, 0] = loss[:-i,:]
    prices[:, i:, 2, 0] = loss[:,:-i]
    prices[:-i, :, 3, 0] = loss[i:,:]
    for i in [2, 3]:
        prices[:, :-i, 0, i - 1] = loss[:,i:] + prices[:, :-i, 0, i - 2]
        prices[i:, :, 1, i - 1] = loss[:-i,:] + prices[i:, :, 1, i - 2]
        prices[:, i:, 2, i - 1] = loss[:,:-i] + prices[:, i:, 2, i - 2]
        prices[:-i, :, 3, i - 1] = loss[i:,:] + prices[:-i, :, 3, i - 2]
    best_prices = np.zeros((height, width, 4), dtype=int) - 1
    best_prices[0, 0, 1] = 0
    best_prices[0, 0, 2] = 0
    price = 0
    #came_from = [[[[], [], [], []] for _ in range(width)] for _ in range(height)]
    while np.all(best_prices[-1, -1, :] == -1) or price < best_prices[-1, -1, best_prices[-1, -1, :] >= 0].min():
        hs, ws, ds = np.where(best_prices == price)
        for i in range(hs.size):
            h, w, dir = hs[i], ws[i], ds[i]
            for ndir in range(4):
                if (dir - ndir) % 2 == 0:
                    continue
                for steps in range(3):
                    nh = h + (steps + 1) * (1 if ndir == 3 else (-1 if ndir == 1 else 0))
                    nw = w + (steps + 1) * (1 if ndir == 0 else (-1 if ndir == 2 else 0))
                    added_price = prices[h, w, ndir, steps]
                    possible_price = price + added_price
                    if nh >= 0 and nw >= 0 and nh < height and nw < width:
                        previous_price = best_prices[nh, nw, ndir]
                        if previous_price == -1 or possible_price < previous_price:
                            best_prices[nh, nw, ndir] = possible_price
                            #came_from[nh][nw][ndir] = [h, w, dir]
        price += 1
    
    result = best_prices[-1, -1, best_prices[-1, -1, :] >= 0].min()
    #h, w, d = height - 1, width - 1, 0 if best_prices[-1, -1, 0] == result else 3
    #while h != 0 or w != 0:
    #    print(best_prices[h, w, d])
    #    print(h, w)
    #    h, w, d = came_from[h][w][d]
    return result

def puzzle2(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    loss = np.array([[int(a) for a in l] for l in lines])
    height, width = loss.shape
    # h, w, dir (0 r, 1 u, 2 l, 3 d), move
    prices = np.zeros((height, width, 4, 11), dtype=int)
    i = 1
    prices[:, :-i, 0, 1] = loss[:,i:]
    prices[i:, :, 1, 1] = loss[:-i,:]
    prices[:, i:, 2, 1] = loss[:,:-i]
    prices[:-i, :, 3, 1] = loss[i:,:]
    for i in range(2, 11):
        prices[:, :-i, 0, i] = loss[:,i:] + prices[:, :-i, 0, i - 1]
        prices[i:, :, 1, i] = loss[:-i,:] + prices[i:, :, 1, i - 1]
        prices[:, i:, 2, i] = loss[:,:-i] + prices[:, i:, 2, i - 1]
        prices[:-i, :, 3, i] = loss[i:,:] + prices[:-i, :, 3, i - 1]
    best_prices = np.zeros((height, width, 4), dtype=int) - 1
    best_prices[0, 0, 1] = 0
    best_prices[0, 0, 2] = 0
    price = 0
    #came_from = [[[[], [], [], []] for _ in range(width)] for _ in range(height)]
    while np.all(best_prices[-1, -1, :] == -1) or price < best_prices[-1, -1, best_prices[-1, -1, :] >= 0].min():
        hs, ws, ds = np.where(best_prices == price)
        for i in range(hs.size):
            h, w, dir = hs[i], ws[i], ds[i]
            for ndir in range(4):
                if (dir - ndir) % 2 == 0:
                    continue
                for steps in range(4, 11):
                    nh = h + steps * (1 if ndir == 3 else (-1 if ndir == 1 else 0))
                    nw = w + steps * (1 if ndir == 0 else (-1 if ndir == 2 else 0))
                    added_price = prices[h, w, ndir, steps]
                    possible_price = price + added_price
                    if nh >= 0 and nw >= 0 and nh < height and nw < width:
                        previous_price = best_prices[nh, nw, ndir]
                        if previous_price == -1 or possible_price < previous_price:
                            best_prices[nh, nw, ndir] = possible_price
                            #came_from[nh][nw][ndir] = [h, w, dir]
        price += 1
    result = best_prices[-1, -1, best_prices[-1, -1, :] >= 0].min()
    #h, w, d = height - 1, width - 1, 0 if best_prices[-1, -1, 0] == result else 3
    #while h != 0 or w != 0:
    #    print(best_prices[h, w, d])
    #    print(h, w)
    #    h, w, d = came_from[h][w][d]
    return result

def main():

    input_file = open("input17.txt")
    input = input_file.read()

    test_input_1 = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = 102
    test_result_2 = 94

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
