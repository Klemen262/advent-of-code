from input17 import data
import numpy as np

# EVERYTHING IS UPSIDE DOWN

shapes = [np.array([[1, 1, 1, 1]]),
np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]]),
np.array([[1], [1], [1], [1]]),
np.array([[1, 1], [1, 1]])]

chamber = np.zeros((10000, 7), dtype=np.int32)
l = len(data)
jet_idx = 0
highest = 0
for i in range(2022):
    shape = shapes[i % 5]
    y = highest + 3
    x = 2
    h, w = shape.shape
    jet = True
    down = False
    while not down:
        if jet:
            if data[jet_idx] == "<" and x >= 1 and (chamber[y : y+h, x-1 : x+w-1] * shape).sum() == 0:
                x -= 1
            elif data[jet_idx] == ">" and x + w <= 6 and (chamber[y : y+h, x+1 : x+w+1] * shape).sum() == 0:
                x += 1
            jet_idx = (jet_idx + 1) % l
        elif y > 0 and (chamber[y-1 : y+h-1, x : x+w] * shape).sum() == 0:
            y -= 1
        else:
            down = True
        jet = not jet
    chamber[y : y+h, x : x+w] = chamber[y : y+h, x : x+w] + shape
    highest = max(highest, y + h)
print(highest)


def new_chamber(chamber: np.ndarray, shape_idx, jet_idx):
    shape = shapes[shape_idx]
    ys = chamber.nonzero()[0]
    highest = 0 if ys.size == 0 else ys.max() + 1
    y = highest + 3
    x = 2
    h, w = shape.shape
    jet = True
    down = False
    while not down:
        if jet:
            if data[jet_idx] == "<" and x >= 1 and (chamber[y : y+h, x-1 : x+w-1] * shape).sum() == 0:
                x -= 1
            elif data[jet_idx] == ">" and x + w <= 6 and (chamber[y : y+h, x+1 : x+w+1] * shape).sum() == 0:
                x += 1
            jet_idx = (jet_idx + 1) % l
        elif y > 0 and (chamber[y-1 : y+h-1, x : x+w] * shape).sum() == 0:
            y -= 1
        else:
            down = True
        jet = not jet
    if y < 1 and highest > chamber_height - 10:
        print("Chamber height is too small, result is wrong!")
    chamber[y : y+h, x : x+w] = chamber[y : y+h, x : x+w] + shape
    highest = max(highest, y + h)
    cut = 0
    if highest > chamber_height - 8:
        cut = highest - (chamber_height - 8)
        chamber[:chamber_height - 8, :] = chamber[cut: highest, :]
        chamber[chamber_height - 8:, :] = 0
    return chamber, cut, jet_idx

l = len(data)
chamber_height = 50
chamber = np.zeros((chamber_height, 7), dtype=np.int32)
deleted_height = 0
shape_idx = 0
jet_idx = 0
seen = {}
found_loop = False
i = 0
num_of_iterations = 1000000000000
state = (tuple(chamber.flatten()), i % 5, jet_idx)
while i < num_of_iterations:
    if found_loop:
        state, d, _, _ = seen[state]
        deleted_height += d
    elif state in seen:
        found_loop = True
        next_state, d, previous_deleted, previous_i = seen[state]
        loop_length = i - previous_i
        loop_count = (num_of_iterations - i) // loop_length
        i += loop_count * loop_length
        deleted_height += loop_count * (deleted_height - previous_deleted) + d
        state = next_state
    else:
        chamber, d, jet_idx = new_chamber(np.array(state[0]).reshape((chamber_height, 7)), state[1], state[2])
        next_state = (tuple(chamber.flatten()), (i + 1) % 5, jet_idx)
        seen[state] = (next_state, d, deleted_height, i)
        deleted_height += d
        state = next_state
    i += 1

print(deleted_height + chamber.nonzero()[0].max() + 1)