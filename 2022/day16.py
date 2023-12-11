from input16 import data
import numpy as np

valves = []
rates = []
paths = []
for line in data.split("\n"):
    words = line.split(" ")
    valves.append(words[1])

n = len(valves)
indexes = {}
for i in range(n):
    indexes[valves[i]] = i

for line in data.split("\n"):
    words = line.split(" ")
    rate = int(line[line.find("=")+1:line.find(";")])
    rates.append(rate)
    ends = [end.strip(",") for end in words[9:]]
    paths.append([indexes[end] for end in ends])

rates = np.array(rates)

distances = np.zeros((n, n), dtype=int) -1
for i in range(n):
    dist = 0
    done = set()
    new = set([i])
    newnew = set()
    while len(done) < n:
        for a in new:
            distances[i, a] = dist
            newnew = newnew.union(set(paths[a]))
        done = done.union(new)
        new = newnew.difference(done)
        newnew = set()
        dist += 1

def max_release(position, timeleft, closed, to_now, best):
    if timeleft <= 0:
        return to_now
    
    if closed.sum() < 1:
        return to_now

    possible_valves = [[valve, rates[valve], distances[position, valve]] for valve in np.where(closed)[0]]
    valve_releases = np.array([[(timeleft - d - 1) * r, d, v] for v, r, d in possible_valves])

    valve_releases = valve_releases[valve_releases[:,0] > 0,:]

    if valve_releases.sum(axis=0)[0] + to_now < best:
        return to_now

    best_now = to_now
    for r, d, v in valve_releases:
        if r <= 0:
            continue
        closed[v] = False
        release = max_release(v, timeleft - d - 1, closed, to_now + r, max(best, best_now))
        closed[v] = True
        best_now = max(release, best_now)
    return best_now

def max_release3(position, timeleft, n, open):
    if timeleft <= 0:
        return 0
    best = 0
    for i in range(n):
        if i in open:
            continue
        d = distances[position, i]
        released = rates[i] * (timeleft - d - 1)
        r = released + max_release3(i, timeleft - d - 1, n, open + [i])
        best = max(r, best)
    return best

def main():
    closed = np.ones(n, dtype=bool)
    closed[rates == 0] = False
    start = indexes["AA"]

    # part 1
    r = max_release(start, 30, closed, 0, 0)
    print(r)

    # part 2 (slow, about 10 min)
    to_split = np.where(closed)[0]
    best_for_two = 0
    for i in range(1, 2 ** (to_split.size - 1)):
        g1, g2 = two_groups(to_split, i)
        closed[g1] = False
        r1 = max_release(start, 26, closed, 0, 0)
        closed[g1] = True

        closed[g2] = False
        r2 = max_release(start, 26, closed, 0, 0)
        closed[g2] = True
        best_for_two = max(best_for_two, r1 + r2)
    print(best_for_two)

def two_groups(all, k):
    # first always in g1
    groups = [[all[0]], []]
    for i in range(1, len(all)):
        groups[k % 2].append(all[i])
        k //= 2
    return groups


if __name__ == "__main__":
    main()