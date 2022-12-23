from input23 import data
import numpy as np

# Takes about 2 minutes to solve

encoding = {".": 0, "#": 1}
grove1 = np.array([[encoding[a] for a in line] for line in data.split("\n")])
padding = 2000
grove_whole = np.zeros((grove1.shape[0] + 2 * padding, grove1.shape[1] + 2 * padding), dtype=np.int8)
grove_whole[padding:-padding,padding:-padding] = grove1

elves_nearby_whole = np.zeros((8, grove_whole.shape[0], grove_whole.shape[1]), dtype=np.int8)
wants_to_move_here_whole = np.zeros_like(grove_whole)
move_whole = np.zeros((4, grove_whole.shape[0], grove_whole.shape[1]), dtype=np.int8)
directions = [[0,1,7], [3,4,5], [5,6,7], [1,2,3]] # N, S, W, E

i = 0
while True:
    current_padding = padding - i - 1
    grove = grove_whole[current_padding:-current_padding,current_padding:-current_padding]
    move = move_whole[:,current_padding:-current_padding,current_padding:-current_padding]
    elves_nearby = elves_nearby_whole[:,current_padding:-current_padding,current_padding:-current_padding]
    wants_to_move_here = wants_to_move_here_whole[current_padding:-current_padding,current_padding:-current_padding]

    elves_nearby[0,1:,:] = grove[:-1,:] # N
    elves_nearby[1,1:,:-1] = grove[:-1,1:] # NE
    elves_nearby[2,:,:-1] = grove[:,1:] # E
    elves_nearby[3,:-1,:-1] = grove[1:,1:] # SE
    elves_nearby[4,:-1,:] = grove[1:,:] # S
    elves_nearby[5,:-1,1:] = grove[1:,:-1] # SW
    elves_nearby[6,:,1:] = grove[:,:-1] # W
    elves_nearby[7,1:,1:] = grove[:-1,:-1] # NW

    to_move = grove * (elves_nearby.sum(axis=0) != 0)
    
    if to_move.sum() == 0:
        print(i + 1)
        break

    move[0,:,:] = to_move * (elves_nearby[directions[(i + 0) % 4],:,:].sum(axis=0) == 0)
    to_move = to_move * (1 - move[0,:,:])
    move[1,:,:] = to_move * (elves_nearby[directions[(i + 1) % 4],:,:].sum(axis=0) == 0)
    to_move = to_move * (1 - move[1,:,:])
    move[2,:,:] = to_move * (elves_nearby[directions[(i + 2) % 4],:,:].sum(axis=0) == 0)
    to_move = to_move * (1 - move[2,:,:])
    move[3,:,:] = to_move * (elves_nearby[directions[(i + 3) % 4],:,:].sum(axis=0) == 0)

    move_N = move[(0 - i) % 4]
    move_S = move[(1 - i) % 4]
    move_W = move[(2 - i) % 4]
    move_E = move[(3 - i) % 4]

    wants_to_move_here[:,:] = 0
    wants_to_move_here[:-1,:] += move_N[1:,:]
    wants_to_move_here[1:,:] += move_S[:-1,:]
    wants_to_move_here[:,:-1] += move_W[:,1:]
    wants_to_move_here[:,1:] += move_E[:,:-1]

    move_N[1:,:] *= wants_to_move_here[:-1,:] == 1
    move_S[:-1,:] *= wants_to_move_here[1:,:] == 1
    move_W[:,1:] *= wants_to_move_here[:,:-1] == 1
    move_E[:,:-1] *= wants_to_move_here[:,1:] == 1

    grove[:-1,:] += move_N[1:,:]
    grove[1:,:] += move_S[:-1,:]
    grove[:,:-1] += move_W[:,1:]
    grove[:,1:] += move_E[:,:-1]

    grove -= move.sum(axis=0)

    i += 1

    if i == 10:
        ys, xs = grove.nonzero()
        print((grove[min(ys):max(ys)+1,min(xs):max(xs)+1] == 0).sum())
        #print("\n".join(["".join(["." if a == 0 else "#" for a in line]) for line in grove[min(ys):max(ys)+1,min(xs):max(xs)+1]]))
