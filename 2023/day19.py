import numpy as np

def puzzle1(input):
    workflows, parts = input.split("\n\n")
    all_workflows = {}
    for workflow in workflows.split("\n"):
        name, rules = workflow.split("{")
        wf = []
        for rule in rules.split(",")[:-1]:
            category = rule[0]
            comparison = rule[1]
            value, true_branch = rule.split(":")
            value = int(value[2:])
            wf.append([category, comparison, value, true_branch])
        wf.append([rules.split(",")[-1][:-1]])
        all_workflows[name] = wf
    
    result = 0
    for part in parts.split("\n")[:-1]:
        cats = part[1:-1].split(",")
        values = {}
        for pair in cats:
            cat, val = pair.split("=")
            val = int(val)
            values[cat] = val
        
        wf_name = "in"
        while wf_name not in "AR":
            wf = all_workflows[wf_name]
            i = 0
            cmp = wf[i]
            while len(cmp) == 4:
                cat, gtlt, val, true_branch = cmp
                if gtlt == ">" and values[cat] > val or gtlt == "<" and values[cat] < val:
                    wf_name = true_branch
                    break
                i += 1
                cmp = wf[i]
            if len(cmp) == 1:
                wf_name = cmp[0]
        
        if wf_name == "A":
            for cat in "xmas":
                result += values[cat]

    return result

def puzzle2(input):
    workflows, parts = input.split("\n\n")
    all_workflows = {}
    borders = {"x": [], "m": [], "a": [], "s": []}
    for workflow in workflows.split("\n"):
        name, rules = workflow.split("{")
        wf = []
        for rule in rules.split(",")[:-1]:
            category = rule[0]
            comparison = rule[1]
            value, true_branch = rule.split(":")
            value = int(value[2:])
            wf.append([category, comparison, value, true_branch])
            if comparison == "<":
                borders[category].append(value)
            else:
                borders[category].append(value + 1)
        wf.append([rules.split(",")[-1][:-1]])
        all_workflows[name] = wf
    for a in "xmas":
        borders[a] = np.unique(np.array(borders[a]))
        borders[a].sort()

    #return solve1(borders, all_workflows)
    initial_limits = {"low": {"x": 1, "m": 1, "a": 1, "s": 1}, "high": {"x": 4001, "m": 4001, "a": 4001, "s": 4001}}
    return solve2(all_workflows, initial_limits)
    
# my original solution, way too slow, took about 30 min
def solve1(borders, all_workflows):
    result = 0
    values = {"x": 1, "m": 1, "a": 1, "s": 1}
    multi = {}
    for a in "xmas":
        multi[a] = borders[a].min() - 1
    end = False
    solved_ms = 0
    while not end:
        current_s_borders = []
        wf_name = "in"
        while wf_name not in "AR":
            wf = all_workflows[wf_name]
            i = 0
            cmp = wf[i]
            while len(cmp) == 4:
                cat, gtlt, val, true_branch = cmp
                if cat == "s":
                    current_s_borders.append(val + (0 if gtlt == "<" else 1))
                if gtlt == ">" and values[cat] > val or gtlt == "<" and values[cat] < val:
                    wf_name = true_branch
                    break
                i += 1
                cmp = wf[i]
            if len(cmp) == 1:
                wf_name = cmp[0]

        s = np.array(sorted(current_s_borders))
        bigger = s[s > values["s"]]
        increase_a = False
        if bigger.size == 0:
            multi["s"] = 4001 - values["s"]
            values["s"] = 1
            increase_a = True
        else:
            next_border = bigger.min()
            multi["s"] = next_border - values["s"]
            values["s"] += multi["s"]
        
        if wf_name == "A":
            result += multi["x"] * multi["m"] * multi["a"] * multi["s"]

        if not increase_a:
            continue

        for cat in "amx":
            if values[cat] + multi[cat] == 4001:
                if cat == "m":
                    solved_ms += 1
                    print(f"solved {solved_ms}/{borders['m'].size}")
                values[cat] = 1
                multi[cat] = borders[cat][0] - 1
                if cat == "x":
                    end = True
            else:
                bigger = borders[cat][borders[cat] > values[cat] + multi[cat]]
                if bigger.size == 0:
                    values[cat] += multi[cat]
                    multi[cat] = 4001 - values[cat]
                else:
                    next_border = bigger.min()
                    values[cat] += multi[cat]
                    multi[cat] = next_border - values[cat]
                break

        if end:
            break
    return result

# much faster one, under 1 second
def solve2(all_workflows, value_limits):
    values = value_limits["low"]
    wf_name = "in"
    while wf_name not in "AR":
        wf = all_workflows[wf_name]
        i = 0
        cmp = wf[i]
        while len(cmp) == 4:
            cat, gtlt, val, true_branch = cmp
            border = val + (0 if gtlt == "<" else 1)
            if border > value_limits["low"][cat] and border < value_limits["high"][cat]:
                previous_high = value_limits["high"][cat]
                previous_low = value_limits["low"][cat]
                value_limits["high"][cat] = border
                r1 = solve2(all_workflows, value_limits)
                value_limits["high"][cat] = previous_high
                value_limits["low"][cat] = border
                r2 = solve2(all_workflows, value_limits)
                value_limits["low"][cat] = previous_low
                return r1 + r2

            if gtlt == ">" and values[cat] > val or gtlt == "<" and values[cat] < val:
                wf_name = true_branch
                break
            i += 1
            cmp = wf[i]
        if len(cmp) == 1:
            wf_name = cmp[0]
    
    if wf_name == "R":
        return 0
    else:
        result = 1
        for a in "xmas":
            result *= value_limits["high"][a] - value_limits["low"][a]
        return result

def main():

    input_file = open("input19.txt")
    input = input_file.read()

    test_input_1 = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = 19114
    test_result_2 = 167409079868000

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(('\033[92m' if result_2 == test_result_2 else '\033[91m') + str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
