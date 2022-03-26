def Read(input_file):
    inFile = open(input_file)
    Sigma = []
    Starting_States = []
    Final_States = []
    NFA = {}
    States = []
    info_read = 0
    while True:
        line = inFile.readline().rstrip()
        if line == "Sigma:":
            line = inFile.readline().rstrip()
            while line != "End":
                Sigma.append(line.rstrip())
                line = inFile.readline().rstrip()
            info_read += 1
        if line == "States:":
            line = inFile.readline().rstrip()
            while line != "End":
                line = list(line)
                States.append(int(line[0]))
                if len(line) > 1:
                    if 'S' in line:
                        Starting_States.append(int(line[0]))
                    if 'F' in line:
                        Final_States.append(int(line[0]))
                line = inFile.readline().rstrip()
            info_read += 1
        if line == "Transitions:":
            line = inFile.readline().rstrip()
            while line != "End":
                line = line.replace(", ", "")
                line = list(line)
                if int(line[0]) not in NFA:
                    NFA[int(line[0])] = {}
                    NFA[int(line[0])][int(line[2])] = []
                    NFA[int(line[0])][int(line[2])].append(line[1])
                else:
                    if int(line[2]) in NFA[int(line[0])]:
                        NFA[int(line[0])][int(line[2])].append(line[1])
                    else:
                        NFA[int(line[0])][int(line[2])] = []
                        NFA[int(line[0])][int(line[2])].append(line[1])
                line = inFile.readline().rstrip()
            info_read += 1
        if info_read == 3:
            break
    return Sigma, Starting_States, Final_States, NFA, States