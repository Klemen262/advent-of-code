from input20 import data
import numpy as np

numbers = np.array([int(a) for a in data.split("\n")])
indexes = [a for a in range(numbers.size)]

for i in range(numbers.size):
    a = indexes.index(i)
    b = a + numbers[i]
    b += numbers[i] // (numbers.size - 1)
    b %= numbers.size
    if a > b:
        indexes = indexes[b+1:a] + indexes[a+1:] + indexes[:b+1] + [i]
    else:
        indexes = indexes[b+1:] + indexes[:a] + indexes[a+1:b+1] + [i]

decrypted = numbers[indexes]
zero = np.where(decrypted == 0)[0][0]
x = decrypted[(zero + 1000) % numbers.size]
y = decrypted[(zero + 2000) % numbers.size]
z = decrypted[(zero + 3000) % numbers.size]
print(x + y + z)


numbers = np.array([int(a) for a in data.split("\n")], dtype=np.int64) * 811589153
indexes = [a for a in range(numbers.size)]

for _ in range(10):
    for i in range(numbers.size):
        a = indexes.index(i)
        b = a + numbers[i]
        b += numbers[i] // (numbers.size - 1)
        b %= numbers.size
        if a > b:
            indexes = indexes[b+1:a] + indexes[a+1:] + indexes[:b+1] + [i]
        else:
            indexes = indexes[b+1:] + indexes[:a] + indexes[a+1:b+1] + [i]

decrypted = numbers[indexes]
zero = np.where(decrypted == 0)[0][0]
x = decrypted[(zero + 1000) % numbers.size]
y = decrypted[(zero + 2000) % numbers.size]
z = decrypted[(zero + 3000) % numbers.size]
print(x + y + z)