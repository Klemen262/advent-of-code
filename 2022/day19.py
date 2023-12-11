from input19 import data
import numpy as np

def puzzle1(input):
    time = 24
    result = 0
    for line in input.split("\n"):
        a, line = line.split(": Each ore robot costs ")
        id = int(a.split(" ")[1])
        # 0 - ore, 1 - clay, 2 - obsidian, 3 - geode
        costs = np.zeros((4, 4), dtype=int)
        a, line = line.split(" ore. Each clay robot costs ")
        costs[0, 0] = int(a)
        a, line = line.split(" ore. Each obsidian robot costs ")
        costs[1, 0] = int(a)
        l1, l2 = line.split(" clay. Each geode robot costs ")
        a, b = l1.split(" ore and ")
        costs[2, 0] = int(a)
        costs[2, 1] = int(b)
        a, line = l2.split(" ore and ")
        costs[3, 0] = int(a)
        a, line = line.split(" ")
        costs[3, 2] = int(a)
        robots = np.array([1, 0, 0, 0])
        resources = np.array([0, 0, 0, 0])
        geodes = max_geode(costs, robots, resources, time, 0)
        result += id * geodes
    return result

def puzzle2(input):
    time = 32
    result = 1
    for line in input.split("\n")[:3]:
        a, line = line.split(": Each ore robot costs ")
        id = int(a.split(" ")[1])
        # 0 - ore, 1 - clay, 2 - obsidian, 3 - geode
        costs = np.zeros((4, 4), dtype=int)
        a, line = line.split(" ore. Each clay robot costs ")
        costs[0, 0] = int(a)
        a, line = line.split(" ore. Each obsidian robot costs ")
        costs[1, 0] = int(a)
        l1, l2 = line.split(" clay. Each geode robot costs ")
        a, b = l1.split(" ore and ")
        costs[2, 0] = int(a)
        costs[2, 1] = int(b)
        a, line = l2.split(" ore and ")
        costs[3, 0] = int(a)
        a, line = line.split(" ")
        costs[3, 2] = int(a)
        robots = np.array([1, 0, 0, 0])
        resources = np.array([0, 0, 0, 0])
        geodes = max_geode(costs, robots, resources, time, 0)
        result *= geodes
    return result

def max_geode(costs, robots, resources, time, best_til_now):
    max_costs = costs.max(axis=0)
    max_resources = resources + robots * time + time * (time - 1) // 2
    if time == 0:
        return resources[3]
    elif time == 1:
        return resources[3] + robots[3]
    elif np.all(costs[3] > max_resources):
        return resources[3] + time * robots[3]
    elif best_til_now > resources[3] + robots[3] * time + time * (time - 1) // 2:
        return 0
    else:
        mm = 0
        for i in range(4):
            if (robots[i] < max_costs[i] or i == 3):
                time_needed = 0
                while np.any(costs[i,:] > resources + robots * time_needed) and time_needed < time - 1:
                    time_needed += 1
                if time_needed < time - 1:
                    robots_II = np.copy(robots)
                    robots_II[i] += 1
                    m = max_geode(costs, robots_II, resources + robots * (time_needed + 1) - costs[i,:], time - time_needed - 1, max(best_til_now, mm))
                    mm = max(mm, m)
        m = resources[3] + robots[3] * time
        mm = max(m, mm)
        return mm

def main():
    print(puzzle1(data))
    print(puzzle2(data))

if __name__ == "__main__":
    main()