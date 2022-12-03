def getPriority(type):
    if (type.islower()):
        return ord(type) - 96
    else:
        return ord(type) - 38

def part1(input):
    sum = 0

    for i in input:
        bagA = set(i[:len(i) // 2])
        bagB = set(i[len(i) // 2:])

        dupe = (bagA & bagB).pop()
        sum += getPriority(dupe) 

    return sum

def part2(input):
    sum = 0

    for i in range(0, len(input) - 2, 3):
        bagA = set(input[i])
        bagB = set(input[i + 1])
        bagC = set(input[i + 2])

        dupe = (bagA & bagB & bagC).pop()
        sum += getPriority(dupe)

    return sum

fp = open("../Input/03_input.txt", "r").read().split("\n")

inputNum = []
for i in fp: 
    inputNum.append(i)

print(part1(inputNum))
print(part2(inputNum))