def part1(input):
    currentCycle = 1
    programCounter = 0
    xRegister = 1
    signal = 0

    for i in input:
        i = i.split()
        programCounter = 1 if (i[0] == "noop") else 2
        
        for j in range(programCounter):
            if (currentCycle % 40 == 20):
                signal += currentCycle * xRegister
            
            if (i[0] == "addx" and j == 1):
                xRegister += int(i[1])

            currentCycle += 1
    
    return signal

def updateSprite(position):
    sprite = ""
    for i in range(1, 41):
        sprite += "█" if (i in range(position, position + 3)) else " "

    return sprite

def part2(input):
    currentCycle = 1
    programCounter = 0
    xRegister = 1
    sprite = updateSprite(xRegister)
    crtScreen = ""

    for i in input:
        i = i.split()
        programCounter = 1 if (i[0] == "noop") else 2
        
        for j in range(programCounter):
            crtScreen += sprite[(currentCycle % 40) - 1]

            if (currentCycle % 40 == 0):
                crtScreen += "\n"

            if (i[0] == "addx" and j == 1):
                xRegister += int(i[1])
                sprite = updateSprite(xRegister)

            currentCycle += 1

    return crtScreen

fp = open("../Input/10_input.txt", "r").read().split("\n")

inputNum = []
for i in fp: 
    inputNum.append(i)

print(part1(inputNum))
print(part2(inputNum))