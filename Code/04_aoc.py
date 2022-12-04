def arrayToInt(array): return [int(i) for i in array]

def part1(input):
    count = 0
    for i in input:
        pair1 = set(range(i[0][0], i[0][1] + 1))
        pair2 = set(range(i[1][0], i[1][1] + 1))

        if (pair1.issubset(pair2) or pair2.issubset(pair1)):
            count += 1

    return count

def part2(input):
    count = 0
    for i in input:
        pair1 = set(range(i[0][0], i[0][1] + 1))
        pair2 = set(range(i[1][0], i[1][1] + 1))        

        if (pair1 & pair2):
            count += 1
    
    return count

fp = open("../Input/04_input.txt", "r").read().split("\n")

inputNum = []
for i in fp: 
    temp = i.split(",")
    temp[0] = arrayToInt(temp[0].split("-"))
    temp[1] = arrayToInt(temp[1].split("-"))

    inputNum.append(temp)

print(part1(inputNum))
print(part2(inputNum))
