def arrayToInt(array): return [int(i) for i in array]

def countCalories(input):
    max = 0
    for i in input:
        if (max < sum(i)):
            max = sum(i)
    return max

def countTopThree(input):
    record = []
    for i in input:
        record.append(sum(i))

    record = sorted(record)

    return sum(record[-3:])

fp = open("../Input/01_input.txt", "r").read().split("\n\n")

inputNum = []
for i in fp: 
    inputNum.append(arrayToInt(i.split("\n")))

print(countCalories(inputNum))
print(countTopThree(inputNum))