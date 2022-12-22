from input22 import data
import numpy as np

board_data, moves_data = data.split("\n\n")
encoding = {" ": 0, ".": 1, "#": 2, "L": -1, "R": 1}
width = max([len(line) for line in board_data.split("\n")])
board = np.array([[encoding[a] for a in line.ljust(width)] for line in board_data.split("\n")])

numbers = [int(a) for a in moves_data.replace("R", " ").replace("L", " ").split(" ")]
turns = []
for a in moves_data:
    if a in "RL":
        turns.append(encoding[a])

# my shape:
#  .##
#  .#.
#  ##.
#  #..

y = 0
x = np.where(board[0] == encoding["."])[0][0]
facing = 0
moveX = {0: 1, 1: 0, 2: -1, 3: 0}
moveY = {0: 0, 1: 1, 2: 0, 3: -1}

for i in range(len(turns) + 1):
    for _ in range(numbers[i]):
        old_x, old_y = x, y
        x += moveX[facing]
        y += moveY[facing]
        if x >= board.shape[1]:
            x = np.nonzero(board[y, :] != encoding[" "])[0][0]
        if y >= board.shape[0]:
            y = np.nonzero(board[:, x] != encoding[" "])[0][0]
        if x < 0:
            x = np.nonzero(board[y, :] != encoding[" "])[0][-1]
        if y < 0:
            y = np.nonzero(board[:, x] != encoding[" "])[0][-1]

        if board[y, x] == encoding[" "]:
            if facing == 0:
                x = np.nonzero(board[y, :] != encoding[" "])[0][0]
            if facing == 1:
                y = np.nonzero(board[:, x] != encoding[" "])[0][0]
            if facing == 2:
                x = np.nonzero(board[y, :] != encoding[" "])[0][-1]
            if facing == 3:
                y = np.nonzero(board[:, x] != encoding[" "])[0][-1]
        
        if board[y, x] == encoding["#"]:
            x, y = old_x, old_y
            break
    if i < len(turns):
        facing = (facing + turns[i]) % 4

print(1000 * (y + 1) + 4 * (x + 1) + facing)

for i in range(len(turns) + 1):
    for _ in range(numbers[i]):
        old_x, old_y = x, y
        old_facing = facing
        # hardcoding every edge, sorry :(
        if y in range(0, 50) and x == 50 and facing == 2: # this is edge number 1, paired with number 9
            y = 149 - y
            x = 0
            facing = 0
        elif y == 0 and x in range(50, 100) and facing == 3: #12
            y = 100 + x
            x = 0
            facing = 0
        elif y == 0 and x in range(100, 150) and facing == 3: #13
            y = 199
            x = old_x - 100
            facing = 3
        elif y == 49 and x in range(100, 150) and facing == 1: #7
            y = x - 50
            x = 99
            facing = 2
        elif y in range(0, 50) and x == 149 and facing == 0: #10
            y = 149 - y
            x = 99
            facing = 2
        elif y in range(50, 100) and x == 50 and facing == 2: #8
            y = 100
            x = old_y - 50
            facing = 1
        elif y in range(50, 100) and x == 99 and facing == 0: #4
            y = 49
            x = old_y + 50
            facing = 3
        elif y == 100 and x in range(0, 50) and facing == 3: #6
            y = x + 50
            x = 50
            facing = 0
        elif y in range(100, 150) and x == 0 and facing == 2: #1
            y = 149 - y
            x = 50
            facing = 0
        elif y in range(100, 150) and x == 99 and facing == 0: #5
            y = 149 - y
            x = 149
            facing = 2
        elif y == 149 and x in range(50, 100) and facing == 1: #14
            y = 100 + x
            x = 49
            facing = 2
        elif y in range(150, 200) and x == 0 and facing == 2: #2
            y = 0
            x = old_y - 100
            facing = 1
        elif y == 199 and x in range(0, 50) and facing == 1: #3
            y = 0
            x = old_x + 100
            facing = 1
        elif y in range(150, 200) and x == 49 and facing == 0: #11
            y = 149
            x = old_y - 100
            facing = 3
        else:
            x += moveX[facing]
            y += moveY[facing]
        
        if board[y, x] == encoding["#"]:
            x, y = old_x, old_y
            facing = old_facing
            break

    if i < len(turns):
        facing = (facing + turns[i]) % 4

print(1000 * (y + 1) + 4 * (x + 1) + facing)
