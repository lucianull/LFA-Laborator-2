import read_module
from stack import Stack

def WordAccept(Word, Starting_States, Final_States, NFA):
    Word = list(Word)
    stack = Stack()
    stack.push(Starting_States[0])
    for letter in Word:
        temp_stack = Stack()
        while stack.size() > 0:
            top = stack.top()
            stack.pop()
            for x in NFA[top].items():
                if letter in x[1]:
                    temp_stack.push(x[0])
        stack = temp_stack
    while stack.size() > 0:
        if stack.top() in Final_States:
            return 1
        stack.pop()
    return 0

def Run(input_file):
    Sigma, Starting_States, Final_States, NFA, States = read_module.Read(input_file)
    Word = input("Introduceti cuvantul: ")
    if WordAccept(Word, Starting_States, Final_States, NFA) == 1:
        print("Cuvantul este acceptat")
    else:
        print("Cuvantul nu este acceptat")

if __name__ == "__main__":
    input_file = "nfa_config_file"
    Run(input_file)