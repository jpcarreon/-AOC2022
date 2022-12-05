def arrayToInt(array): 
    newArray = []
    for i in array:
        try:
            newArray.append(int(i))
        except:
            newArray.append(i)
    return newArray

def dictDeepCopy(dictionary): return {i: j.copy() for i,j in dictionary.items()}

def part1(table, moves):
    for i in moves.split("\n"):
        currentMove = arrayToInt(i.split())
        
        for i in range(0, currentMove[1]):
            table[currentMove[5]].insert(0, table[currentMove[3]].pop(0))
            
    result = ""
    for i in table.values():
        result += i[0]
    
    return result

def part2(table, moves):
    for i in moves.split("\n"):
        currentMove = arrayToInt(i.split())

        taken = table[currentMove[3]][0:currentMove[1]]

        for i in range(len(taken), 0, -1):
            table[currentMove[5]].insert(0, taken[i - 1])
            table[currentMove[3]].pop(0)
            
    result = ""
    for i in table.values():
        result += i[0]
    
    return result

fp = open("../Input/05_input.txt", "r").read().split("\n\n")

stacks = {}
fp[0] = fp[0].split("\n")
for i in fp[0][-1].split():
    stacks[int(i)] = []

for i in fp[0][:-1]:
    idx = 1

    ta = i.split(" ")
    new = ""

    for j in ta:
        if (j != ""):
            new += j
        new += " "

    for i in range(1, len(new), 4):
        if new[i] != " ":
            stacks[idx].append(new[i])
        
        idx += 1

print(part1(dictDeepCopy(stacks), fp[1]))
print(part2(dictDeepCopy(stacks), fp[1]))