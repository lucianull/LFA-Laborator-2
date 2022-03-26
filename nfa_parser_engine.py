import read_module
from stack import Stack

def ValidateNFA(input_file):
    Sigma, Starting_States, Final_States, NFA, States = read_module.Read(input_file)
    if len(Starting_States) > 1:
        return 0
    for x in NFA.items():
        if x[0] not in States:
            return 0
        for y in x[1].items():
            if y[0] not in States:
                return 0
            for z in y[1]:
                if z not in Sigma:
                    return 0
    stack = Stack()
    freq = [0 for i in range(len(States))]
    freq[Starting_States[0]] = 1
    stack.push(Starting_States[0])
    while stack.size() > 0:
        top = stack.top()
        stack.pop()
        if top in Final_States:
            return 1
        if top in NFA:
            for x in NFA[top].keys():
                if freq[x] == 0:
                    stack.push(x)
                    freq[x] = 1
    return 0

def Run(input_file):
    if ValidateNFA(input_file) == 0:
        print("NFA-ul nu este valid")
    else:
        print("NFA-ul este valid")


if __name__ == "__main__":
    input_file = "nfa_config_file"
    Run(input_file)