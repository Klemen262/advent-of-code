from input24 import data
import numpy as np

encoding = {"#": 0, ".": 1, "^": 2, "v": 3, "<": 4, ">": 5}
start_valley = np.array([[encoding[a] for a in line] for line in data.split("\n")])
blizzards_up = start_valley[1:-1,1:-1] == encoding["^"]
blizzards_down = start_valley[1:-1,1:-1] == encoding["v"]
blizzards_left = start_valley[1:-1,1:-1] == encoding["<"]
blizzards_right = start_valley[1:-1,1:-1] == encoding[">"]

possible_locations = np.zeros_like(blizzards_up)
new_possible_locations = np.zeros_like(blizzards_up)
blizzards = np.zeros_like(blizzards_up)
h, w = blizzards.shape

minute = 1
while possible_locations[-1,-1] == 0:
    blizzards[:h - (minute % h),:] = blizzards_up[minute % h:,:]
    blizzards[h - (minute % h):,:] = blizzards_up[:minute % h,:]
    blizzards[minute % h:,:] += blizzards_down[:h - (minute % h),:]
    blizzards[:minute % h,:] += blizzards_down[h - (minute % h):,:]
    blizzards[:,:w - (minute % w)] += blizzards_left[:,minute % w:]
    blizzards[:,w - (minute % w):] += blizzards_left[:,:minute % w]
    blizzards[:,minute % w:] += blizzards_right[:,:w - (minute % w)]
    blizzards[:,:minute % w] += blizzards_right[:,w - (minute % w):]

    new_possible_locations[:,:] = possible_locations[:,:]
    new_possible_locations[0,0] = 1
    new_possible_locations[:-1,:] += possible_locations[1:,:]
    new_possible_locations[1:,:] += possible_locations[:-1,:]
    new_possible_locations[:,:-1] += possible_locations[:,1:]
    new_possible_locations[:,1:] += possible_locations[:,:-1]
    possible_locations = (new_possible_locations > 0) * (blizzards == 0)
    minute += 1
print(minute)

# mostly copy paste of first while loop
# added time increment, reset possible locations and changed indexes of start and end
minute += 1
possible_locations[:,:] = 0
while possible_locations[0,0] == 0: # changed indexes from end to start
    blizzards[:h - (minute % h),:] = blizzards_up[minute % h:,:]
    blizzards[h - (minute % h):,:] = blizzards_up[:minute % h,:]
    blizzards[minute % h:,:] += blizzards_down[:h - (minute % h),:]
    blizzards[:minute % h,:] += blizzards_down[h - (minute % h):,:]
    blizzards[:,:w - (minute % w)] += blizzards_left[:,minute % w:]
    blizzards[:,w - (minute % w):] += blizzards_left[:,:minute % w]
    blizzards[:,minute % w:] += blizzards_right[:,:w - (minute % w)]
    blizzards[:,:minute % w] += blizzards_right[:,w - (minute % w):]

    new_possible_locations[:,:] = possible_locations[:,:]
    new_possible_locations[-1,-1] = 1 # also changed indexes here
    new_possible_locations[:-1,:] += possible_locations[1:,:]
    new_possible_locations[1:,:] += possible_locations[:-1,:]
    new_possible_locations[:,:-1] += possible_locations[:,1:]
    new_possible_locations[:,1:] += possible_locations[:,:-1]
    possible_locations = (new_possible_locations > 0) * (blizzards == 0)
    minute += 1
#print(minute)

minute += 1
possible_locations[:,:] = 0
# literal copy paste of first loop
while possible_locations[-1,-1] == 0:
    blizzards[:h - (minute % h),:] = blizzards_up[minute % h:,:]
    blizzards[h - (minute % h):,:] = blizzards_up[:minute % h,:]
    blizzards[minute % h:,:] += blizzards_down[:h - (minute % h),:]
    blizzards[:minute % h,:] += blizzards_down[h - (minute % h):,:]
    blizzards[:,:w - (minute % w)] += blizzards_left[:,minute % w:]
    blizzards[:,w - (minute % w):] += blizzards_left[:,:minute % w]
    blizzards[:,minute % w:] += blizzards_right[:,:w - (minute % w)]
    blizzards[:,:minute % w] += blizzards_right[:,w - (minute % w):]

    new_possible_locations[:,:] = possible_locations[:,:]
    new_possible_locations[0,0] = 1
    new_possible_locations[:-1,:] += possible_locations[1:,:]
    new_possible_locations[1:,:] += possible_locations[:-1,:]
    new_possible_locations[:,:-1] += possible_locations[:,1:]
    new_possible_locations[:,1:] += possible_locations[:,:-1]
    possible_locations = (new_possible_locations > 0) * (blizzards == 0)
    minute += 1
print(minute)