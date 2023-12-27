import numpy as np

def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    
    vertices = set()
    edges = {}

    for line in lines:
        start, ends = line.split(": ")
        vertices.add(start)
        for end in ends.split(" "):
            vertices.add(end)
            edges[start] = edges.get(start, set())
            edges[start].add(end)
            edges[end] = edges.get(end, set())
            edges[end].add(start)

    # find one of those three wires
    to_break = False
    for v in vertices:
        for end in edges[v]:
            used = set()
            used.add((v, end))
            used.add((end, v))
            paths = at_least_n_paths(edges, v, end, 3, used)
            if len(paths) < 3:
                used.add((v, end))
                used.add((end, v))
                to_break = True
                break
        if to_break:
            break
    
    # find other two, they must be in previously found paths
    for i in range(len(paths[0]) - 1):
        for j in range(len(paths[1]) - 1):
            new_used = set()
            new_used.add((paths[0][i], paths[0][i + 1]))
            new_used.add((paths[0][i + 1], paths[0][i]))
            new_used.add((paths[1][j], paths[1][j + 1]))
            new_used.add((paths[1][j + 1], paths[1][j]))
            if len(find_path(edges, paths[0][0], paths[0][-1], used.union(new_used))) == 0:
                n1 = len(number_of_accesible(edges, paths[0][0], used.union(new_used)))
                n2 = len(vertices) - n1
                return n1 * n2
    return 0
                
def number_of_accesible(edges, start, used):
    accesible = set()
    new_accesible = set()
    new_accesible.add(start)
    while len(new_accesible) > 0:
        accesible = accesible.union(new_accesible)
        now_accesible = new_accesible
        new_accesible = set()
        for v_from in now_accesible:
            for v_to in edges[v_from]:
                if (v_to, v_from) not in used:
                    if v_to not in accesible:
                        new_accesible.add(v_to)
    return accesible

def at_least_n_paths(edges, start, end, n, used=set()):
    used.add((start, end))
    used.add((end, start))
    paths = []
    for _ in range(n):
        path = find_path(edges, start, end, used)
        if len(path) > 1:
            paths.append(path)
            for i in range(len(path) - 1):
                used.add((path[i], path[i + 1]))
                used.add((path[i + 1], path[i]))
        else:
            return paths
    return paths

def find_path(edges, start, end, used_edges):
    came_from = {}
    accesible = set()
    new_accesible = set()
    new_accesible.add(start)
    while len(new_accesible) > 0 and end not in accesible:
        accesible = accesible.union(new_accesible)
        now_accesible = new_accesible
        new_accesible = set()
        for v_from in now_accesible:
            for v_to in edges[v_from]:
                if (v_to, v_from) not in used_edges:
                    if v_to not in accesible:
                        new_accesible.add(v_to)
                        came_from[v_to] = v_from
                    if v_to == end:
                        this = v_to
                        previous = v_from
                        reverse_path = [v_to]
                        while previous != start:
                            this = previous
                            previous = came_from[this]
                            reverse_path.append(this)
                        reverse_path.append(start)
                        return reverse_path[::-1]
    return []

def main():

    input_file = open("input25.txt")
    input = input_file.read()

    test_input_1 = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""

    test_result_1 = 54

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

if __name__ == "__main__":
    main()
