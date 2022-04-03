import read_module
from stack import Stack

def CreateSigmaRow(DFATransitionTable, Sigma):
    for letter in Sigma:
        DFATransitionTable[letter] = []
def CreateState(array):
    if len(array) > 1:
        array.sort()
        string = ''
        for x in array:
            string = string + ',' + str(x)
        return '{' + string[1:] + '}'
    else:
        return str(array[0])

def PrintDFA(DFATransitionTable, Sigma, StartingState, FinalStates, ConversionDict):
    print("Sigma:")
    for letter in Sigma:
        print(letter)
    print("End")
    print("States:")
    for state in DFATransitionTable.keys():
        start = 0
        final = 0
        if StartingState in ConversionDict[state]:
            start = 1
        for x in FinalStates:
            if x in ConversionDict[state]:
                final = 1
                break
        if start == 1 and final == 1:
            print(state + ', S, F')
        else:
            if final == 1:
                print(state + ', F')
            elif start == 1:
                print(state + ', S')
            else:
                print(state)
    print("End")
    print("Transitions:")
    for x in DFATransitionTable.items():
        for y in DFATransitionTable[x[0]].items():
            print(x[0] + ', ' + y[0] + ', ' + y[1])
    print("End")


def Run(input_file):
    Sigma, Starting_States, Final_States, NFA, States = read_module.Read(input_file)
    NFATransitionTable = {}
    for state in States:
        NFATransitionTable[state] = {}
        for letter in Sigma:
            NFATransitionTable[state][letter] = []
    for x in NFA.keys():
        for y in NFA[x].keys():
            for z in NFA[x][y]:
                NFATransitionTable[x][z].append(y)
    ConversionDict = {}
    DFATransitionTable = {}
    DFATransitionTable[str(Starting_States[0])] = {}
    ConversionDict[str(Starting_States[0])] = Starting_States
    stack = Stack()
    DeathState = '-1'
    for x in NFATransitionTable[Starting_States[0]].items():
        if len(x[1]) > 0:
            state = CreateState(x[1])
            if state not in DFATransitionTable:
                stack.push(state)
                ConversionDict[state] = x[1]
                DFATransitionTable[str(Starting_States[0])][x[0]] = state
        else:
            DFATransitionTable[str(Starting_States[0])][x[0]] = DeathState

    while stack.size() != 0:
        top = stack.top()
        stack.pop()
        if top not in DFATransitionTable:
            DFATransitionTable[top] = {}
            temp_dict = {}
            CreateSigmaRow(temp_dict, Sigma)
            for x in ConversionDict[top]:
                 for state in NFATransitionTable[x].items():
                     if len(state[1]) > 0:
                         for y in state[1]:
                             if y not in temp_dict[state[0]]:
                                temp_dict[state[0]].append(y)
            for state in temp_dict.items():
                if len(state[1]) > 0:
                    s = CreateState(state[1])
                    ConversionDict[s] = state[1]
                    DFATransitionTable[top][state[0]] = s
                    if s not in DFATransitionTable:
                        stack.push(s)
                else:
                    DFATransitionTable[top][state[0]] = DeathState
    DFATransitionTable[DeathState] = {}
    DFATransitionTable[DeathState]['a'] = DeathState
    DFATransitionTable[DeathState]['b'] = DeathState
    DFATransitionTable[DeathState]['c'] = DeathState
    ConversionDict['-1'] = [-1]
    PrintDFA(DFATransitionTable, Sigma, Starting_States[0], Final_States, ConversionDict)

if __name__ == "__main__":
    input_file = "nfa_config_file"
    Run(input_file)