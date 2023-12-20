import numpy as np

class Module:

    def __init__(self, module_type, module_name, out_connections):
        self.module_name = module_name
        self.module_type = module_type
        self.out_connections = out_connections
        self.in_connections = []
        self.turned_on = False
        self.to_send_out = None
        self.in_signals = []
        self.remembered_signals = {}

    def new_in_connection(self, module_name):
        if module_name not in self.in_connections:
            self.in_connections.append(module_name)
            self.remembered_signals[module_name] = "low"
    
    def in_signal(self, module, signal):
        self.in_signals.append([module, signal])
        self.remembered_signals[module] = signal
    
    def process_signals(self, i=0, highs=None):
        if highs != None:
            # hardcoded module vf, last before output
            if self.module_name == "vf" and "high" in [b for a, b in self.in_signals]:
                high_module = list(filter(lambda x: x[1] == "high", self.in_signals))[0][0]
                highs[high_module].add(i)
        
        if self.module_type == "%":
            if "low" in [b for a, b in self.in_signals]:
                self.turned_on = not self.turned_on
                self.to_send_out =  "high" if self.turned_on else "low"
            self.in_signals = []
        elif self.module_type == "&":
            if len(self.in_signals) > 0:
                if "low" in self.remembered_signals.values():
                    self.to_send_out = "high"
                else:
                    self.to_send_out = "low"
                self.in_signals = self.in_signals[1:]
        elif self.module_type == "b":
            self.to_send_out = self.in_signals[0][1] if len(self.in_signals) > 0 else None
            self.in_signals = []
        
        return False
    
    def send_signals(self, modules):
        sent = [0, 0]
        if self.to_send_out != None:
            for out in self.out_connections:
                modules[out].in_signal(self.module_name, self.to_send_out)
                sent[0 if self.to_send_out == "low" else 1] += 1
            self.to_send_out = None
            return sent[0], sent[1], self.out_connections
        return sent[0], sent[1], []


def puzzle1(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    modules = {}
    for line in lines:
        module, connections = line.split(" -> ")
        module_type = module[0]
        module_name = module[1:]
        if module_name == "roadcaster":
            module_name = "broadcaster"
        out_connections = connections.split(", ")
        modules[module_name] = Module(module_type, module_name, out_connections)
    output_module = None
    for module in modules.keys():
        for out_con in modules[module].out_connections:
            if out_con not in modules.keys():
                output_module = Module("o", out_con, [])
                continue
            modules[out_con].new_in_connection(module)
    if output_module != None:
        modules[output_module.module_name] = output_module
    sent = [0, 0]
    for i in range(1000):
        modules["broadcaster"].in_signal("button", "low")
        sent[0] += 1
        queue = ["broadcaster"]
        while len(queue) > 0:
            module = modules[queue[0]]
            queue = queue[1:]
            module.process_signals()
            l, h, outs = module.send_signals(modules)
            queue += outs
            sent[0] += l
            sent[1] += h
    return sent[0] * sent[1]

def puzzle2(input):
    lines = input.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    modules = {}
    for line in lines:
        module, connections = line.split(" -> ")
        module_type = module[0]
        module_name = module[1:]
        if module_name == "roadcaster":
            module_name = "broadcaster"
        out_connections = connections.split(", ")
        modules[module_name] = Module(module_type, module_name, out_connections)
    output_module = None
    for module in modules.keys():
        for out_con in modules[module].out_connections:
            if out_con not in modules.keys():
                output_module = Module("o", out_con, [])
                continue
            modules[out_con].new_in_connection(module)
    if output_module != None:
        modules[output_module.module_name] = output_module
    # hardcoded module names for inputs to last module before output
    highs = {"mk": set(), "pm": set(), "hf": set(), "pk": set()}
    for i in range(1, 10000):
        modules["broadcaster"].in_signal("button", "low")
        queue = ["broadcaster"]
        while len(queue) > 0:
            module = modules[queue[0]]
            queue = queue[1:]
            module.process_signals(i, highs)
            _, _, outs = module.send_signals(modules)
            queue += outs

    first_highs = [min(vals) for vals in highs.values()]
    lcm_of_first_appearance_of_high = np.lcm.reduce(first_highs)
    return lcm_of_first_appearance_of_high


def main():

    input_file = open("input20.txt")
    input = input_file.read()

    test_input_1 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

    #test_input_2 = """"""
    test_input_2 = test_input_1

    test_result_1 = 11687500
    #test_result_2 = 1

    result_1 = puzzle1(test_input_1)
    #print(result_1)
    print(('\033[92m' if result_1 == test_result_1 else '\033[91m') + str(puzzle1(input)) + '\033[0m')

    #result_2 = puzzle2(test_input_2)
    #print(result_2)
    print(str(puzzle2(input)) + '\033[0m')

if __name__ == "__main__":
    main()
