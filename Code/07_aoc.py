import os; os.system("cls")
import re

def parseFileSystem(input):
    files = {"/": {"SIZE": 0}}
    pwd = []

    for i in input:
        i = i.split()
        
        if (i[0] == "$"):
            if (i[1] == "cd"):
                if (i[2] == ".."):
                    pwd.pop()
                else:
                    pwd.append(i[2])
        else:
            fp = files
            for j in pwd:
                fp = fp[j]

            if (i[0] == "dir"):
                fp[i[1]] = {"SIZE": 0}

            else:
                fp[i[1]] = int(i[0])
                
                fp = files
                for j in pwd:
                    fp[j]["SIZE"] += int(i[0])
                    fp = fp[j]
    return files

def parseFileSystemSize(input):
    files = {"/": 0}
    pwd = []

    for i in input:
        i = i.split()

        if (i[0] == "$"):
            if (i[1] == "cd"):
                if (i[2] == ".."):
                    pwd.pop()
                else:
                    pwd.append(i[2])
        else:
            current = "/"
            for j in pwd[1:]:
                current += j + "/"

            
            if (i[0] == "dir"):
                files[current + i[1]] = 0

            else:
                for x in files.keys():
                    if (current.startswith(x)):
                        files[x] += int(i[0])
                        
    return files

def part1Helper(files, sum):
    for i, j in files.items():
        if i == "SIZE" and j <= 100000: 
            sum += j

        elif (isinstance(j, dict)):
            sum += part1Helper(j, 0)
            
    return sum

def part1(files):
    sum = 0
    for i, j in files["/"].items():
        if i == "SIZE" and j <= 100000: 
            sum += j

        elif (isinstance(j, dict)):
            sum += part1Helper(j, 0)

    return sum

def part2Helper(files, minimum, unusedSpace, needed):
    for i, j in files.items():
        if i == "SIZE" and  unusedSpace + j >= needed: 
            minimum = min(j, minimum)

        elif (isinstance(j, dict)):
            minimum = part2Helper(j, minimum, unusedSpace, needed)

    return minimum

def part2(files):
    minimum = 9999999999
    unusedSpace = 70000000 - files["/"]["SIZE"]
    needed = 30000000
    
    for i, j in files["/"].items():
        if i == "SIZE" and  unusedSpace + j >= needed: 
            minimum = min(j, minimum)

        elif (isinstance(j, dict)):
            minimum = part2Helper(j, minimum, unusedSpace, needed)

    return minimum

def silverAndGold(files):
    unusedSpace = 70000000 - files["/"]
    needed = 30000000

    silver = sum([i for i in files.values() if i <= 100000])
    gold = min([i for i in files.values() if unusedSpace + i >= needed])

    return [silver, gold]


fp = open("../Input/07_input.txt", "r").read().split("\n")

inputNum = []
for i in fp: 
    inputNum.append(i)

files = parseFileSystem(inputNum)

#print(silverAndGold(files))

print(part1(files))
print(part2(files))