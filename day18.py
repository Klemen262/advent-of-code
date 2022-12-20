from input18 import data
import numpy as np

coordinates = np.array([[int(a) for a in b.split(",")] for b in data.split("\n")])

droplet = np.zeros(coordinates.max(axis=0) + 1, dtype=bool)
for i in range(coordinates.shape[0]):
    droplet[tuple(coordinates[i])] = True

connected = 0
connected += (droplet[:,:,1:] * droplet[:,:,:-1]).sum()
connected += (droplet[:,1:,:] * droplet[:,:-1,:]).sum()
connected += (droplet[1:,:,:] * droplet[:-1,:,:]).sum()

surface = coordinates.shape[0] * 6 - connected * 2
print(surface)

# water on edges
water = np.zeros_like(droplet)
water[(1, -1),:,:] = 1 - droplet[(1, -1),:,:]
water[:,(1, -1),:] = 1 - droplet[:,(1, -1),:]
water[:,:,(1, -1)] = 1 - droplet[:,:,(1, -1)]

a, b, c = droplet.shape
air_count = a * b * c - droplet.sum() - water.sum()
new_air_count = air_count
air_count += 1

# water leaking in from all 6 directions
while (new_air_count < air_count):
    air_count = new_air_count
    # water[here] = water[here] or water[neighbour] and not droplet[here]
    water[:,:,1:] = water[:,:,1:] + water[:,:,:-1] * (1 - droplet[:,:,1:])
    water[:,1:,:] = water[:,1:,:] + water[:,:-1,:] * (1 - droplet[:,1:,:])
    water[1:,:,:] = water[1:,:,:] + water[:-1,:,:] * (1 - droplet[1:,:,:])
    water[:,:,:-1] = water[:,:,:-1] + water[:,:,1:] * (1 - droplet[:,:,:-1])
    water[:,:-1,:] = water[:,:-1,:] + water[:,1:,:] * (1 - droplet[:,:-1,:])
    water[:-1,:,:] = water[:-1,:,:] + water[1:,:,:] * (1 - droplet[:-1,:,:])
    new_air_count = a * b * c - droplet.sum() - water.sum()

air = (1 - water) * (1 - droplet)

dry = 0
dry += (droplet[:,:,1:] * air[:,:,:-1]).sum()
dry += (droplet[:,1:,:] * air[:,:-1,:]).sum()
dry += (droplet[1:,:,:] * air[:-1,:,:]).sum()
dry += (droplet[:,:,:-1] * air[:,:,1:]).sum()
dry += (droplet[:,:-1,:] * air[:,1:,:]).sum()
dry += (droplet[:-1,:,:] * air[1:,:,:]).sum()
print(surface - dry)