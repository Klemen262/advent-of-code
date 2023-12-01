from input12 import data
import numpy as np

lines = [line for line in data.split("\n")]
map = np.array([[ord(a) for a in line] for line in lines])

start = np.where(map == ord("S"))
end = np.where(map == ord("E"))
map[start] = ord("a")
map[end] = ord("z")
left = np.zeros_like(map, dtype=bool)
right = np.zeros_like(map, dtype=bool)
up  = np.zeros_like(map, dtype=bool)
down = np.zeros_like(map, dtype=bool)
up[1:,:] = map[:-1, :] <= map[1:, :] + 1
down[:-1,:] = map[1:, :] <= map[:-1, :] + 1
left[:,1:] = map[:, :-1] <= map[:, 1:] + 1
right[:,:-1] = map[:, 1:] <= map[:, :-1] + 1

n = 0
rechable_in_n_plus_1_moves = np.zeros_like(map, dtype=bool)
rechable_in_n_moves = np.zeros_like(map, dtype=bool)
rechable_in_n_moves[start] = True
while not rechable_in_n_plus_1_moves[end]:
    rechable_in_n_plus_1_moves[:-1,:] += (up * rechable_in_n_moves)[1:,:]
    rechable_in_n_plus_1_moves[1:,:] += (down * rechable_in_n_moves)[:-1,:]
    rechable_in_n_plus_1_moves[:,:-1] += (left * rechable_in_n_moves)[:,1:]
    rechable_in_n_plus_1_moves[:,1:] += (right * rechable_in_n_moves)[:,:-1]
    rechable_in_n_moves[:,:] = rechable_in_n_plus_1_moves[:,:]
    n += 1
print(n)

n = 0
rechable_in_n_plus_1_moves[:,:] = False
rechable_in_n_moves[:,:] = False
rechable_in_n_moves[map == ord("a")] = True
while not rechable_in_n_plus_1_moves[end]:
    rechable_in_n_plus_1_moves[:-1,:] += (up * rechable_in_n_moves)[1:,:]
    rechable_in_n_plus_1_moves[1:,:] += (down * rechable_in_n_moves)[:-1,:]
    rechable_in_n_plus_1_moves[:,:-1] += (left * rechable_in_n_moves)[:,1:]
    rechable_in_n_plus_1_moves[:,1:] += (right * rechable_in_n_moves)[:,:-1]
    rechable_in_n_moves[:,:] = rechable_in_n_plus_1_moves[:,:]
    n += 1
print(n)