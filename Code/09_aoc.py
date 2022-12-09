def ropeMovement(input, length):
    ropePosition = {i: [0, 0] for i in range(0, length + 1)}
    visited = {(0, 0)}
    dirs = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}

    for i in input:
        i = i.split()
        
        for _ in range(int(i[1])):
            ropePosition[0][0] += dirs[i[0]][0]
            ropePosition[0][1] += dirs[i[0]][1]

            for rope, curr in ropePosition.items():
                if (rope == 0): continue
                prev = ropePosition[rope - 1]

                if (abs(prev[0] - curr[0]) > 1 or abs(prev[1] - curr[1]) > 1):
                    if (abs(prev[0] - curr[0]) >= 1 and abs(prev[1] - curr[1]) >= 1):
                        curr[0] += 1 if (prev[0] - curr[0] > 0) else -1
                        curr[1] += 1 if (prev[1] - curr[1] > 0) else -1

                        if (rope == length): visited.add((curr[0], curr[1]))

                    elif (abs(prev[0] - curr[0]) > 1):
                        curr[0] += 1 if (prev[0] - curr[0] > 0) else -1

                        if (rope == length): visited.add((curr[0], curr[1]))
                    
                    elif (abs(prev[1] - curr[1]) > 1):
                        curr[1] += 1 if (prev[1] - curr[1] > 0) else -1

                        if (rope == length): visited.add((curr[0], curr[1]))

    return len(visited)

fp = open("../Input/09_input.txt", "r").read().split("\n")

inputNum = []
for i in fp: 
    inputNum.append(i)

print(ropeMovement(inputNum, 1))
print(ropeMovement(inputNum, 9))