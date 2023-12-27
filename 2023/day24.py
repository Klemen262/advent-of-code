import numpy as np
from sympy import Symbol, Eq, solve

def puzzle1(input, low, high):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    n = len(lines)
    points = np.zeros((n, 3))
    velocities = np.zeros((n, 3))
    for i in range(n):
        line = lines [i]
        point, velocity = line.split(" @ ")
        px, py, pz = point.split(", ")
        vx, vy, vz = velocity.split(", ")
        points[i, :] = (int(px), int(py), int(pz))
        velocities[i, :] = (int(vx), int(vy), int(vz))

    result = 0
    for i in range(n):
        for j in range(i + 1, n):


            intersect = intersection_2d(points[i,:], velocities[i,:], points[j,:], velocities[j,:])
            if type(intersect) == np.ndarray and (intersect >= low).all() and (intersect <= high).all():
                result += 1
    return result

def intersection_2d(p1, v1, p2, v2):
    determinant = (v2[1] * v1[0] - v2[0] * v1[1])
    if determinant == 0:
        return None
    else:
        u, t = np.linalg.solve(np.hstack((np.array([v2]).T, np.array([v1]).T))[:2,:], np.array([p1 - p2]).T[:2,:])
        if u > 0 and t < 0:
            return (p1 - t * v1)[:2]
        else:
            return None

#def time_intersection(p1, v1, p2, v2):
#    determinant = (v2[1] * v1[0] - v2[0] * v1[1])
#    if determinant == 0:
#        return None
#    else:
#        u, t = np.linalg.solve(np.hstack((np.array([v2]).T, np.array([v1]).T))[:2,:], np.array([p1 - p2]).T[:2,:])
#        if u != -t:
#            return None
#        elif (((p1 - t * v1) - (p2 + u * v2)) < 1e-10).all():
#            return (p1 - t * v1)
#        else:
#            return None

#def intersection(p1, v1, p2, v2):
#    determinant = (v2[1] * v1[0] - v2[0] * v1[1])
#    if determinant == 0:
#        return None
#    else:
#        u, t = np.linalg.solve(np.hstack((np.array([v2]).T, np.array([v1]).T))[:2,:], np.array([p1 - p2]).T[:2,:])
#        a.append(max(np.abs((p1 - t * v1) - (p2 + u * v2))))
#        if (np.abs((p1 - t * v1) - (p2 + u * v2)) < 1e-5).all():
#            return (p1 - t * v1)
#        else:
#            return None

def puzzle2(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    n = len(lines)
    points = np.zeros((n, 3))
    velocities = np.zeros((n, 3))
    for i in range(3):
        line = lines [i]
        point, velocity = line.split(" @ ")
        px, py, pz = point.split(", ")
        vx, vy, vz = velocity.split(", ")
        points[i, :] = (int(px), int(py), int(pz))
        velocities[i, :] = (int(vx), int(vy), int(vz))

    a = Symbol("a")
    b = Symbol("b")
    c = Symbol("c")
    d = Symbol("d")
    e = Symbol("e")
    f = Symbol("f")
    t1 = Symbol("t1")
    t2 = Symbol("t2")
    t3 = Symbol("t3")

    a1, b1, c1 = points[0]
    a2, b2, c2 = points[1]
    a3, b3, c3 = points[2]
    d1, e1, f1 = velocities[0]
    d2, e2, f2 = velocities[1]
    d3, e3, f3 = velocities[2]

    solution = solve([
        Eq(a1 + t1 * d1, a + t1 * d),
        Eq(b1 + t1 * e1, b + t1 * e),
        Eq(c1 + t1 * f1, c + t1 * f),
        Eq(a2 + t2 * d2, a + t2 * d),
        Eq(b2 + t2 * e2, b + t2 * e),
        Eq(c2 + t2 * f2, c + t2 * f),
        Eq(a3 + t3 * d3, a + t3 * d),
        Eq(b3 + t3 * e3, b + t3 * e),
        Eq(c3 + t3 * f3, c + t3 * f)
    ])[0]

    return int(solution[a] + solution[b] + solution[c])

def main():

    input_file = open("input24.txt")
    input = input_file.read()

    test_input_1 = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = 2
    test_result_2 = 47

    result_1 = puzzle1(test_input_1, 7, 27)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input, 200000000000000, 400000000000000)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()



