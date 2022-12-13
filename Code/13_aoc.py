import os
os.system("cls")
print("\n\nNEW INPUT\n")

def isInOrder(left, right):
    maxLen = max(len(left), len(right))

    for i in range(maxLen):
        if (i == len(left) and i < len(right)):
            return True
        elif (i == len(right) and i < len(left)):
            return False

        lval = left[i]
        rval = right[i]

        if (isinstance(lval, int) and isinstance(rval, int)):
            if lval < rval:
                return True
            elif lval > rval:
                return False

        elif (isinstance(lval, list) and isinstance(rval, list)):
            ordered = isInOrder(lval, rval)
            if ordered is not None: return ordered

        elif (isinstance(lval, list)):
            ordered = isInOrder(lval, [rval])
            if ordered is not None: return ordered

        elif (isinstance(rval, list)):
            ordered = isInOrder([lval], rval)
            if ordered is not None: return ordered
        
    return None

def part1(input):
    sumParts = 0
    for i in range(len(input)):
        left, right = input[i]

        if isInOrder(left, right):
            sumParts += i + 1

    return sumParts


def part2(input):
    packets = [[[2]], [[6]]]
    temp = None
    answer = 1

    for i in input:
        packets.append(i[0])
        packets.append(i[1])

    for i in range(len(packets)):
        for j in range(len(packets) - i - 1):
            if not isInOrder(packets[j], packets[j + 1]):
                temp = packets[j]
                packets[j] = packets[j + 1]
                packets[j + 1] = temp
        
    for i in range(len(packets)):
        if packets[i] == [[2]]:
            answer *= i + 1
        elif packets[i] == [[6]]:
            answer *= i + 1
    
    return answer

fp = open("../Input/13_input.txt", "r").read().split("\n\n")

inputNum = []
for i in fp: 
    np = [eval(j) for j in i.split("\n")]
    inputNum.append(np)

print(part1(inputNum))
print(part2(inputNum))