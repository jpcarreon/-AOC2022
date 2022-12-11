import math
import re

class Monkey:
    def __init__(self, items, operation, test, t, f):
        self.items = items.copy()
        self.operation = operation.split()
        self.test = test
        self.t = t
        self.f = f
        self.count = 0
        
def arrayToInt(array): 
    newArray = []
    for i in array:
        try:
            newArray.append(int(i))
        except:
            newArray.append(i)
    return newArray

def part1(monkeys):
    for _ in range(20):        
        for i in monkeys:
            for _ in range(len(i.items)):
                i.count += 1
                worry = i.items.pop(0)
                op2 = worry if (i.operation[2] == "old") else int(i.operation[2])
                worry = worry + op2 if (i.operation[1] == "+") else worry * op2
                worry //= 3

                if (worry % i.test == 0):
                    monkeys[i.t].items.append(worry)
                else:
                    monkeys[i.f].items.append(worry)

    count = sorted([i.count for i in monkeys])
    return count[-1] * count[-2]

def part2(input):
    modMonkey = math.prod([j.test for j in input])
    
    for _ in range(10000):        
        for i in input:
            for _ in range(len(i.items)):
                i.count += 1
                worry = i.items.pop(0)
                op2 = worry if (i.operation[2] == "old") else int(i.operation[2])
                worry = worry + op2 if (i.operation[1] == "+") else worry * op2
                worry %= modMonkey

                if (worry % i.test == 0):
                    input[i.t].items.append(worry)
                else:
                    input[i.f].items.append(worry)

    count = sorted([i.count for i in input])
    return count[-1] * count[-2]

fp = open("../Input/11_input.txt", "r").read().split("\n\n")

inputNum = []
for i in fp: 
    inputNum.append(i)

MonkeyList = []
MonkeyList2 = []
for i in inputNum:
    i = i.split("\n")

    items = arrayToInt(re.sub(r",", "", i[1]).split()[2:])
    operation = i[2].split(" = ")[1]
    test = int(i[3].split()[-1])
    t = int(i[4].split()[-1])
    f = int(i[5].split()[-1])

    MonkeyList.append(Monkey(items, operation, test, t, f))
    MonkeyList2.append(Monkey(items, operation, test, t, f))

print(part1(MonkeyList))
print(part2(MonkeyList2))